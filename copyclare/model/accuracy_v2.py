"""
Contributors: Adi Bozzhanov, Tianhao Chen

"""

import json
import math
import os
import time

import cv2
import statsmodels.api as sm

from copyclare.common import AppSingleton
from copyclare.data import DATA_DIR

from .pose_module import PoseModule


def round_decimals_up(number: float, decimals: int = 1):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places needs to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10**decimals
    return math.ceil(number * factor) / factor


class AccuracyModel:

    joints_map = {
        "left_elbow": 13,
        "right_elbow": 14,
        "left_shoulder": 11,
        "right_shoulder": 12,
    }

    joint_adjacent = {
        "left_elbow": (15, 11),
        "right_elbow": (12, 16),
        "left_shoulder": (13, 12),
        "right_shoulder": (11, 14),
    }

    def __init__(self, exercise, joints):
        self.detector = PoseModule()
        self.joints = joints

        if exercise.angles_json == "-1":
            pass
        elif exercise.angles_json != "null":
            self.angles = json.loads(exercise.angles_json)

        video = cv2.VideoCapture(DATA_DIR + exercise.video_directory)
        if not video.isOpened():
            print("Error Opening a video file")
        fps = video.get(cv2.CAP_PROP_FPS)
        self.step = 1 / fps

        self.offset = 20

    def _init_angles(self):
        angles = {}
        for joint in self.joints:
            angles[joint] = {}
        return angles

    def get_angles(self, video_path):
        """
        Initialises angles json for an exercise video

        Args:
            vieo_path: absolute path to the video

        Returns:
            a dictionary where each key is a joint and value is a
            list of angle/time pairs
        """

        angles = self._init_angles()

        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            print("Error Opening a video file")
        fps = video.get(cv2.CAP_PROP_FPS)
        self.step = 1 / fps
        count = 0
        while video.isOpened():
            success, frame = video.read()
            if not success:
                print("Can't read video")
                break

            for joint in self.joints:
                t = count / fps
                person = self.detector.find_person(frame)
                landmark_list = self.detector.find_landmarks(person,
                                                             draw=False)
                a = self.find_angle(person, joint, landmark_list)
                angles[joint][round_decimals_up(t, 4)] = a
            count += 1

        self.duration = count / fps

        # Smoothing with local regression
        for joint in self.joints:
            tmp = []
            for time_stamp in angles[joint]:
                tmp.append(angles[joint][time_stamp])

            lowess = sm.nonparametric.lowess(tmp,
                                             list(angles[joint].keys()),
                                             frac=0.1)
            ts, angs = list(lowess[:, 0]), list(lowess[:, 1])
            for i in range(len(ts)):
                angles[joint][str(ts[i])] = angs[i]

        return angles

    def color_frame(self, frame, landmark_list, accuracy):
        """
        Draws a skeleton on top of the user.

        Args:
           frame: opencv frame containing an image to be colored.
           landmark_list: Contains coordinates of landmarks of interest
           accuracy: a real number that's used to determine the color of
               the skeleton
        """
        done = set()
        clr = (255, 255, 255) if (accuracy > 90) else (0, 0, 0)
        if landmark_list:
            for joint in self.joints:
                x, y = landmark_list[self.joints_map[joint]][1:]
                x_left, y_left = landmark_list[self.joint_adjacent[joint]
                                               [0]][1:]
                x_right, y_right = landmark_list[self.joint_adjacent[joint]
                                                 [1]][1:]

                p1 = (x, y)
                p2 = (x_left, y_left)
                if not (p1, p2) in done and not (p2, p1) in done:
                    cv2.line(frame, p1, p2, clr, 5)
                    done.add((p1, p2))

                p2 = (x_right, y_right)
                if not (p1, p2) in done and not (p2, p1) in done:
                    cv2.line(frame, p1, p2, clr, 5)
                    done.add((p1, p2))

                cv2.circle(frame, (x, y), 5, clr, cv2.FILLED)

    def find_angle(self, frame, joint, landmark_list):
        """
        Finds an angle of any given joint.

        Args:
            frame: OpenCV frame
            joint: String value representing the joing
            landmark_list: mediapipe landmark_list
        """

        angle = -1
        if len(landmark_list) != 0:
            middle = self.joints_map[joint]
            left, right = self.joint_adjacent[joint]
            angle = self.detector.find_angle(frame,
                                             left,
                                             middle,
                                             right,
                                             draw=False)

        return angle

    def get_accuracy(self, angle, reltime, joint):
        """
        Calculats the accuracy given the angle, joint and the relative time.

        Args:

            angle: float angle value
            reltime: float timestamp within the range (0-duration of the video)
            joint: String value representing the joint to be considered.

        Reurns:
            accuracy value in the range 0-100
        """
        form_time = round_decimals_up(int(reltime / self.step) * self.step, 4)
        a1 = angle
        rep = False
        if str(form_time) in self.angles[joint]:
            a2 = self.angles[joint][str(form_time)]
            accuracy = 100 - (abs((a1 - a2)) / ((a1 + a2) / 2) * 100)
        else:
            rep = True
            accuracy = 100

        return accuracy, rep

    def accuracy(self, frame, reltime):
        person = self.detector.find_person(frame)
        landmark_list = self.detector.find_landmarks(person, draw=False)
        accuracy = 0

        for joint in self.joints:

            angle = self.find_angle(person, joint, landmark_list)
            acc, rep = self.get_accuracy(angle, reltime, joint)
            accuracy += acc
        accuracy /= len(self.joints)

        self.color_frame(person, landmark_list, accuracy)

        return accuracy, rep

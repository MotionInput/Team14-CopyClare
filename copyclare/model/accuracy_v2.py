import time
from collections import deque

import cv2
import statsmodels.api as sm
import math


from copyclare.model import PoseModule


def round_decimals_up(number:float, decimals:int=1):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places needs to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10 ** decimals
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

    def __init__(self, video_path, joints):
        self.detector = PoseModule()
        self.joints = joints
        self.angles = self.get_angles(video_path)
        self.camera_buffer = deque()

    def _init_angles(self):
        angles = {}
        for joint in self.joints:
            angles[joint] = {}
        return angles

    def get_angles(self, video_path):
        """
        Returns:
            a dictionary where each key is a joint and value is a
            list of angle/time pairs
        """

        angles = self._init_angles()

        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            print("Error Opening a video file")
        fps = video.get(cv2.CAP_PROP_FPS)
        count = 0
        while video.isOpened():
            success, frame = video.read()
            if not success:
                print("Can't read video")
                break

            for joint in self.joints:
                t = count / fps
                person = self.detector.find_person(frame)
                landmark_list = self.detector.find_landmarks(person, draw=False)
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
                angles[joint][ts[i]] = angs[i]

        return angles

    def color_frame(self, frame, landmark_list):
        done = set()
        
        for joint in self.joints:
            x, y = landmark_list[self.joints_map[joint]][1:]
            x_left, y_left = landmark_list[self.joint_adjacent[joint][0]][1:]
            x_right, y_right = landmark_list[self.joint_adjacent[joint][1]][1:]
            cv2.circle(frame, (x, y), 5, (255, 0, 0), cv2.FILLED)

            p1 = (x,y)
            p2 = (x_left, y_left)
            if not (p1, p2) in done and not(p2,p1) in done:
                cv2.line(frame, p1, p2, (255, 255, 255), 5)
                done.add((p1,p2))

            p2 = (x_right, y_right)
            if not (p1, p2) in done and not(p2,p1) in done:
                cv2.line(frame, p1, p2, (255, 255, 255), 5)
                done.add((p1,p2))




    def find_angle(self, frame, joint, landmark_list):
        if len(landmark_list) != 0:
            middle = self.joints_map[joint]
            left, right = self.joint_adjacent[joint]
            angle = self.detector.find_angle(frame,
                                             left,
                                             middle,
                                             right,
                                             draw=False)
            return angle

    def check_angle(self, angle, reltime):

        

        
        return 

    def accuracy(self, frame):
        person = self.detector.find_person(frame)
        landmark_list = self.detector.find_landmarks(person, draw=False)
        accuracy = 0
        
        
        for joint in self.joints:
            self.find_angle(person, joint, landmark_list)

        self.color_frame(person, landmark_list)

        return accuracy

    def buffer_duration(self):
        if len(self.camera_buffer) < 2:
            return 0
        else:
            return self.camera_buffer[-1][0] - self.camera_buffer[0][0]

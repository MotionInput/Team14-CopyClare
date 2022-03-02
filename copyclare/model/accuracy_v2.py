import time
from collections import deque

import cv2
import statsmodels.api as sm
import math

from copyclare.model import PoseModule


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
            angles[joint] = [[], []]
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
                a = self.find_angle(frame, joint)
                angles[joint][0].append(a)
                angles[joint][1].append(t)
            count += 1

        self.duration = count / fps

        # Smoothing with local regression
        for joint in self.joints:
            lowess = sm.nonparametric.lowess(angles[joint][0],
                                             angles[joint][1],
                                             frac=0.1)
            ts, angs = list(lowess[:, 0]), list(lowess[:, 1])
            angles[joint][0] = angs
            angles[joint][1] = ts

        return angles

    def color_frame(self, frame):

        for joint in self.joints_map:

            x, y = self.detector.landmark_list[self.joints_map[joint]][1:]
            cv2.circle(frame, (x, y), 5, (255, 0, 0), cv2.FILLED)

        pass

    def find_angle(self, frame, joint):
        person = self.detector.find_person(frame)
        landmark_list = self.detector.find_landmarks(person, draw=False)
        if len(landmark_list) != 0:
            middle = self.joints_map[joint]
            left, right = self.joint_adjacent[joint]
            angle = self.detector.find_angle(person,
                                             left,
                                             middle,
                                             right,
                                             draw=False)
            return angle

    def accuracy(self, frame):

        accuracy = 0
        for joint in self.joints:
            self.find_angle(frame, joint)

        return accuracy

    def buffer_duration(self):
        if len(self.camera_buffer) < 2:
            return 0
        else:
            return self.camera_buffer[-1][0] - self.camera_buffer[0][0]

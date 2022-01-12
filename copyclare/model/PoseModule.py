import numpy as np
import mediapipe as mp


class PoseModule():
    def __init__(self, mode=False, up_body=False, smooth=True,
                 detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.up_body = up_body
        self.smooth = smooth
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.mode, self.up_body, self.smooth,
                                      self.detection_con, self.track_con)

    def find_person(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(
                img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS
            )
        return img
        pass

    def find_landmarks(self, img, draw=True):

        pass

    def find_angle(self, img, p1, p2, p3, draw=True):
        pass

    def output_angle(self, angle):
        pass

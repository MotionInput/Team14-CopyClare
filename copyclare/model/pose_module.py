from cmath import acos
import numpy as np
import mediapipe as mp
import cv2
import math


class PoseModule:
    def __init__(
        self,
        mode=False,
        up_body=False,
        smooth=True,
        detection_con=True,
        track_con=True,
        smooth_segmentation=False,
    ):

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=True,
            model_complexity=1,
            smooth_landmarks=True,
            enable_segmentation=False,
        )

    def find_person(self, img, draw=False):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(img, self.results.pose_landmarks,
                                        self.mp_pose.POSE_CONNECTIONS)
        return img

    def find_landmarks(self, img, draw=True):
        self.landmark_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.landmark_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.landmark_list

    def find_angle(self, img, p1, p2, p3, draw=True):
        # Get the landmarks
        z1, x1, y1 = self.landmark_list[p1]
        z2, x2, y2 = self.landmark_list[p2]
        z3, x3, y3 = self.landmark_list[p3]
        len12 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        len23 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2 + (z2 - z3)**2)
        len13 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2 + (z1 - z3)**2)
        # Calculate the Angle
        angle = math.degrees(
            math.acos((len12**2 + len23**2 - len13**2) / 2 / len12 / len23))
        if angle < 0:
            angle += 360

        # Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 5)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 5)
            cv2.circle(img, (x1, y1), 11, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 16, (255, 60, 0), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 16, (255, 60, 0), 2)
            cv2.circle(img, (x3, y3), 11, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 16, (255, 60, 0), 2)

            #cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 60),
            #            cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)
        return angle

    def store_data(self, frame_num, angle):
        output_file = open(frame_num + ".csv", mode="a")
        output_file.write(angle + " , ")
        output_file.close()

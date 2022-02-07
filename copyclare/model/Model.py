import csv
from email import header
import math
import cv2
from .PoseModule import PoseModule
import numpy as np
import os


class Model:
    def __init__(self, is_live_video=True, input_video_filepath=None):
        self.input_video_filepath = input_video_filepath
        if is_live_video:
            self.cap = cv2.VideoCapture(0)
        else:
            self.cap = cv2.VideoCapture(input_video_filepath)
        if not self.cap.isOpened():
            print("Cannot open video")
            exit()
        self.detector = PoseModule()
        self.score = []

    def show_capture(self):
        while self.cap.isOpened():
            success, frame = self.cap.read()
            # if frame is read correctly success is True
            if not success:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            person = self.detector.find_person(frame)
            landmark_list = self.detector.find_landmarks(person, draw=False)
            # print(landmark_list)
            angle = 0
            if len(landmark_list) != 0:
                cv2.circle(person,
                           (landmark_list[13][1], landmark_list[13][2]), 15,
                           (0, 0, 255), cv2.FILLED)

                angle = self.detector.find_angle(person, 11, 13, 15)
            # cv2.imshow("Image", person)
            yield person, angle
            if cv2.waitKey(1) == ord('q'):
                break
        self.close_capture()

    def gather_video_angle_data(self, csv_name):
        try:
            with open(csv_name, mode="r") as f:
                reader = csv.reader(f)
                row_num = 0
                data_set = []
                for row in reader:
                    row_num += 1
                    if row_num % 7 == 0:
                        data_set.append([])
                    data_set[-1].append({
                        "landmark_num": row[0],
                        "coordinates": row[1]
                    })
                return data_set
        except FileNotFoundError:
            print("the corresponding csv file is no found!")

    def store_video_angle_data(self, landmark_list):
        file_name = os.path.basename(self.input_video_filepath)
        portion = os.path.splitext(file_name)
        new_name = portion[0] + ".csv"
        with open(new_name, mode="a") as f:
            writer = csv.writer(f)

            for coordinate in landmark_list:
                writer.writerow([landmark_list.index(coordinate), coordinate])

    def close_capture(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def get_video_angle_data(self, data_set, landmark_num1, landmark_num2,
                             landmark_num3):
        video_angle_data = []
        for data in data_set:
            for dict in data:
                if dict["landmark_num"] == landmark_num1:
                    p1 = np.array(dict["coordinate"])
                if dict["landmark_num"] == landmark_num2:
                    p2 = np.array(dict["coordinate"])
                if dict["landmark_num"] == landmark_num3:
                    p3 = np.array(dict["coordinate"])
                v1 = p1 - p2
                v2 = p3 - p2
                dot_product = np.dot(v1, v2)
                angle = math.degrees(
                    math.acos(dot_product / np.linalg.norm(v1) /
                              np.linalg.norm(v2)))

            video_angle_data.append(angle)
        return video_angle_data

    def compare_accuracy(self, frame_num, video_angle_data, ture_angle, score):
        for angle in video_angle_data:
            if video_angle_data.index(angle) == frame_num:
                accuracy = ture_angle / angle
                score.append(accuracy)
                return accuracy
            else:
                print("can not find the corresponding angle")

    def compare_completeness(self, video_angle_data, angle):
        angles_in_ED = [x[1] for x in video_angle_data]
        max_angle = max(angles_in_ED)
        min_angle = min(angles_in_ED)
        return (angle - min_angle) / (max_angle - min_angle)

    def cal_total_score(self):
        total_accuracy = 0
        for accuracy in self.score:
            total_accuracy += accuracy
        return total_accuracy / len(self.score)


# def main():
# # read from a video file
# reharb_video_path = 'vtest.avi'
# reharb_video = cv2.VideoCapture(reharb_video_path)
# detector = posture_detector()
# while reharb_video.isOpened():
#     success, frame = reharb_video.read()
#     # if frame is read correctly success is True
#     if not success:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     person = detector.find_person(frame)
#     landmark_list = detector.find_landmarks(person,draw=False)
#     print(landmark_list)
#     if len(landmark_list)!=0:
#         cv2.circle(person, (landmark_list[14][1],landmark_list[14][2]),15,(0,0,255),cv2.FILLED)
#     cv2.imshow("Image",person)
#     if cv2.waitKey(1) == ord('q'):
#         break

# read from camera

# while True:
#     # Capture frame-by-frame
#     success, frame = cap.read()
#     # if frame is read correctly, success is True
#     if not success:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     # gray = cv2  .cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

if __name__ == '__main__':
    model = Model()
    model.show_capture()

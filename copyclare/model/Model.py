import cv2
from PoseModule import PoseModule


class Model:
    def __init__(self, is_live_video=True, input_video_filepath=None):
        if is_live_video:
            self.cap = cv2.VideoCapture(0)
        else:
            self.cap = cv2.VideoCapture(input_video_filepath)
        if not self.cap.isOpened():
            print("Cannot open video")
            exit()
        self.detector = PoseModule()

    def show_capture(self):
        while self.cap.isOpened():
            success, frame = self.cap.read()
            # if frame is read correctly success is True
            if not success:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            person = self.detector.find_person(frame)
            landmark_list = self.detector.find_landmarks(person, draw=False)
            print(landmark_list)
            if len(landmark_list) != 0:
                cv2.circle(
                    person, (landmark_list[14][1], landmark_list[14][2]), 15, (0, 0, 255), cv2.FILLED)
            cv2.imshow("Image", person)
            if cv2.waitKey(1) == ord('q'):
                break
        self.close_capture()

    def gather_exercise_data(self):
        pass

    def store_exercise_data(self):
        pass

    def close_capture(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def compare_accuracy(self):
        pass

    def compare_completeness(self):
        pass


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

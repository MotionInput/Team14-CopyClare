import mediapipe as mp
import cv2
import numpy as np

class posture_detector():
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
    
    def find_person(self,img,draw=True):
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(
                img,self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS
            )
        return img
        pass
    
    def find_landmarks(self,img,draw=True):
        
        pass
    
    def find_angle(self,img,p1,p2,p3,draw=True):
        pass
    
    def Output_angle(self,angle):
        pass




def main():
    # read from a video file
    reharb_video_path = 'vtest.avi'
    reharb_video = cv2.VideoCapture(reharb_video_path)
    detector = posture_detector()
    while reharb_video.isOpened():
        success, frame = reharb_video.read()
        # if frame is read correctly success is True
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        person = detector.find_person(frame)
        landmark_list = detector.find_landmarks(person,draw=False)
        print(landmark_list)
        if len(landmark_list)!=0:
            cv2.circle(person, (landmark_list[14][1],landmark_list[14][2]),15,(0,0,255),cv2.FILLED)
        cv2.imshow("Image",person)        
        if cv2.waitKey(1) == ord('q'):
            break
    reharb_video.release()
    cv2.destroyAllWindows()


"""# read from camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    success , frame = cap.read()
    # if frame is read correctly, success is True
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()"""

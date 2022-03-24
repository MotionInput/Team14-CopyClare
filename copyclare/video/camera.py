import cv2
import time

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, QRect

from copyclare.model import AccuracyModel, PoseModule
from copyclare import DATA_PATH


class CameraThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, container, exercise):
        QThread.__init__(self, None)
        self.container = container
        self._running = True
        self.worker = CameraWorker(exercise)

    def run(self):

        for frame in self.worker.work():
            if not self._running:
                break
            _, _, width, height = self.container.frameGeometry().getRect()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)

            scaled_img = img.scaled(width, height,
                                    Qt.KeepAspectRatioByExpanding)

            self.update_frame.emit(scaled_img)
        self.quit()


class CameraWorker:
    def __init__(self, exercise):

        self.exercise = exercise
        joints = {
            "left_shoulder",
            "left_elbow",
        }
        self.model = AccuracyModel(exercise, joints)

        self.detector = PoseModule()


    def work(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error opening a video file")

        self.beginning = time.time()
        self.accuracy = 0
        self.num_of_repetitions = 0

        start = time.time()

        init = 0
        coo_dict = {}

        while (cap.isOpened):

            success, frame = cap.read()
            
            #take down the 10th frame as the background of the heatmap
            if init < 25:
                self.hp = frame
                init += 1
            else:
                person = self.detector.find_person(frame)
                landmark_list = self.detector.find_landmarks(person,draw=False)
                self.heatmap(coo_dict,self.hp,landmark_list)
                #cv2.imshow("Image", self.hp)

            correct = self.model.accuracy(frame, time.time() - start)

            if correct:
                self.accuracy += 1
                self.num_of_repetitions += 1
            else:
                start = time.time()

            if not success:
                print("Can't read from Camera")

            frame = cv2.flip(frame, 1)

            yield frame
    
    def heatmap(self, coo_dict, hp, landmark_list):
        
        if len(landmark_list) != 0:
            landmark = landmark_list[13]
            S_landmark = self.trans_cooList_keyString(landmark)
            
            if not S_landmark in coo_dict:
                coo_dict.update({S_landmark:1})
                cv2.circle(hp,(landmark_list[13][1], landmark_list[13][2]),3,(0,255,255),cv2.FILLED)
            else:
                # print("overlap")
                num = coo_dict[S_landmark] + 1
                coo_dict[S_landmark] = num
                cv2.circle(hp,(landmark_list[13][1], landmark_list[13][2]),4,(0,255-num*25,255),cv2.FILLED)
                
        #cv2.imshow("Image", heatmap)

    def trans_cooList_keyString(self,cooList):
        z,x,y = cooList[:]
        return "%f+%f+%f"%(z,x//10*10,y//10*10)

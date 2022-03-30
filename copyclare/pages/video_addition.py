import json
import os
import sys
import time

import cv2

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QImage, QPixmap

from copyclare.common import AppSingleton
from copyclare.data.objects import Exercise
from copyclare.model.accuracy_v2 import AccuracyModel
from copyclare.pyui.video_addition import Ui_video_addition

from copyclare import UiElement
from copyclare.data import DATA_DIR
from copyclare.video.video import VideoWorker


class VideoAddition(UiElement):
    def __init__(self, master):
        super().__init__(master, "video_addition", Ui_video_addition)

        self.app = AppSingleton.get_app()

        # video_name = self.ui.video_name_editor.getText()
        # video_description = self.ui.description_editor.getText()
        # video_tags = self.ui.tags_editor.getText()

        self.ui.back_button.clicked.connect(
            lambda x: self.app.load_page("home"))
        self.ui.browse_button.clicked.connect(self.open_file)
        self.ui.upload_button.clicked.connect(self.upload)
        self.ui.confirm_button.clicked.connect(self.confirm)
        self.ui.cut_button.clicked.connect(self.cut)
        self.ui.start_slider.setMinimum(0)
        self.ui.start_slider.setMaximum(100)
        self.ui.start_slider.valueChanged[int].connect(self.change_display_start)
        self.ui.end_slider.setMinimum(0)
        self.ui.end_slider.setMaximum(100)
        self.ui.end_slider.valueChanged[int].connect(self.change_display_end)

        self.ui.input_area.setVisible(False)
        self.ui.video_trimmer.setVisible(False)

        self.exercise = Exercise(None,None,None,None,None,None)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select video file",
            DATA_DIR + "/videos", "video files(*.mp4)")
        self.fileName = "/"+os.path.relpath(fileName,DATA_DIR)
        #print(self.fileName)
        self.ui.input_area.setVisible(True)
        self.ui.video_trimmer.setVisible(True)

        self.ui.browse_button.setStyleSheet(
            "QPushButton{background-color: rgb(186, 186, 186);}")

        cap = cv2.VideoCapture(DATA_DIR+self.fileName)
        if not cap.isOpened():
            print("Error opening a video file")        
        self.frames = []        
        while (cap.isOpened):
            success, frame = cap.read()
            #print(frame_count)
            if not success:
                print("Can't read from Camera")
                break            
            self.frames.append(frame)

    def upload(self):
        joints = [
            "left_elbow", "left_shoulder", "right_elbow", "right_shoulder"
        ]
        accuracymodel = AccuracyModel(self.exercise,joints)
        self.exercise.angles_json = json.dumps(accuracymodel.get_angles(self.exercise.video_directory))
        # print(exercise.angles_json)
        self.app.db.add_exercise(self.exercise)        
        self.app.load_page("home")
        pass

    def confirm(self):
        video_name = self.ui.video_name_editor.toPlainText()
        description = self.ui.description_editor.toPlainText()
        # tags = self.ui.tags_editor.toPlainText()
        # tag = tags.split(",")

        self.exercise.name = video_name
        self.exercise.video_directory = self.fileName
        self.exercise.description = description
        

        self.ui.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(0, 255, 127);}")

    def generate_video(self,frames,end_frame_num):
        videoWriter = cv2.VideoWriter(DATA_DIR+self.fileName,cv2.VideoWriter_fourcc(*'mp4v'),30,(1920,1080))
        for frame in frames:
            index = frames.index(frame)
            if index > end_frame_num:
                break
            if index == 0:
                cv2.imwrite(self.exercise.name+".png")
            videoWriter.write(frame)

    def change_display_start(self):
        value = self.ui.start_slider.value()
        frame_num = round(value/100 *(len(self.frames)+1))
        frame = self.frames[frame_num]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        Qimg = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
        self.ui.video.setPixmap(QPixmap.fromImage(Qimg))
    
    def change_display_end(self):
        value = self.ui.end_slider.value()
        frame_num = round(value/100 *(len(self.frames)+1))
        frame = self.frames[frame_num]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        Qimg = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
        self.ui.video.setPixmap(QPixmap.fromImage(Qimg))



    def cut(self):
        self.video_state = 0

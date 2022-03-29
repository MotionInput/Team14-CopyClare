import json
import os
import sys

import cv2

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QImage, QPixmap

from copyclare.common import AppSingleton
from copyclare.data.objects import Exercise
from copyclare.model.accuracy_v2 import AccuracyModel
from copyclare.pyui.video_addition import Ui_video_addition

from copyclare import UiElement
from copyclare.data import DATA_DIR


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
        self.ui.play_button.clicked.connect(self.play)
        self.ui.cut_button.clicked.connect(self.cut)

        self.ui.input_area.setVisible(False)
        self.ui.video_trimmer.setVisible(False)

        self.exercise = Exercise(None,None,None,None,None,None)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select video file",
            os.getcwd() + "/data/videos", "video files(*.mp4)")
        self.fileName = os.path.relpath(fileName,DATA_DIR)
        # print(self.fileName)
        self.ui.input_area.setVisible(True)
        self.ui.video_trimmer.setVisible(True)

        self.ui.browse_button.setStyleSheet(
            "QPushButton{background-color: rgb(186, 186, 186);}")

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

    def play(self):
        self.frame_counter = 0
        vidcap = cv2.VideoCapture(DATA_DIR+self.fileName)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        videoWriter = cv2.VideoWriter(DATA_DIR+self.fileName,cv2.VideoWriter_fourcc('M','P',"4",'V'),fps,(1920,1080))
        self.video_state = 1
        while vidcap.isOpened() and self.video_state == 1:
             
            success, image = vidcap.read()
            #print(success)
            if success:
                self.frame_counter += 1
                videoWriter.write(image)
                if self.frame_counter == 1:
                    self.exercise.image_directory = f"{DATA_DIR}/videos/{self.exercise.name}.png"
                    cv2.imwrite(self.exercise.image_directory, image)
                    self.ui.video.setPixmap(QPixmap.fromImage(image))
                else:
                    self.ui.video.setPixmap(QPixmap.fromImage(image))
        
        vidcap.release()

    def cut(self):
        self.video_state = 0

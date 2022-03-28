import os
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget

from copyclare.common import AppSingleton
from copyclare.model.accuracy_v2 import AccuracyModel
from copyclare.data.objects import Exercise

from .page import Page


class VideoAddition(Page):
    def __init__(self, master):
        super().__init__(master, "video_addition")

        self.app = AppSingleton.get_app()

        # video_name = self.ui.video_name_editor.getText()
        # video_description = self.ui.description_editor.getText()
        # video_tags = self.ui.tags_editor.getText()

        self.ui.back_button.clicked.connect(
            lambda x: self.app.load_page("home"))
        self.ui.browse_button.clicked.connect(self.open_file)
        self.ui.upload_button.clicked.connect(self.upload)
        self.ui.confirm_button.clicked.connect(self.confirm)
        self.ui.input_area.setVisible(False)
        self.ui.video_trimmer.setVisible(False)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.ui.video)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select video file",
            os.getcwd() + "/data/videos", "video files(*.mp4)")
        self.fileName = fileName

        self.ui.input_area.setVisible(True)
        self.ui.video_trimmer.setVisible(True)

        self.ui.browse_button.setStyleSheet(
            "QPushButton{background-color: rgb(186, 186, 186);}")

        #self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()

    def upload(self):
        exercise = Exercise(None, self.video_name, self.fileName, "None",
                            self.description, "-1")
        joints = [
            "left_elbow", "left_shoulder", "right_elbow", "right_shoulder"
        ]
        # accuracymodel = AccuracyModel(exercise,joints)
        # exercise.angles_json = accuracymodel.get_angles(exercise.video_directory)
        self.app.db.add_exercise(exercise)
        self.ui.upload_button.clicked.connect(
            lambda x: self.app.load_page("home"))
        pass

    def confirm(self):
        self.video_name = self.ui.video_name_editor.toPlainText()
        self.description = self.ui.description_editor.toPlainText()
        tags = self.ui.tags_editor.toPlainText()
        self.tag = tags.split(",")

        self.ui.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(0, 255, 127);}")

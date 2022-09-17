"""
Contributors: Adi Bozzhanov, Tianhao Chen

"""

import json
import os

import cv2

from PySide6 import QtWidgets
from PySide6.QtGui import QImage, QPixmap

from copyclare.common import AppSingleton
from copyclare.data.database import Exercise
from copyclare.model.accuracy_v2 import AccuracyModel
from copyclare.pyui.video_addition import Ui_video_addition
from copyclare.video import ProcessingThread

from copyclare import UiElement
from copyclare.data import DATA_DIR


class VideoAddition(UiElement):
    """
    Initialise the video addition page.

    Allows user to browse videos, enter information,
    trim video, and upload to database.

    Args:
        master (ParentWidget): The frame in which the page will be displayed in.

    """

    def __init__(self, master):
        super().__init__(master, "video_addition", Ui_video_addition)

        self.app = AppSingleton.get_app()
        self.session = self.app.db.Session()

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
        self.ui.end_slider.setValue(99)
        self.ui.end_slider.valueChanged[int].connect(self.change_display_end)

        self.ui.input_area.setVisible(False)
        self.ui.video_trimmer.setVisible(False)

        self.h = None
        self.w = None

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select video file",
            DATA_DIR + "/videos", "video files(*.mp4)")
        self.fileName = "/"+os.path.relpath(fileName,DATA_DIR).replace("\\", "/")
        #print(self.fileName)
        self.ui.input_area.setVisible(True)
        self.ui.video_trimmer.setVisible(True)

        self.ui.browse_button.setStyleSheet(
            "QPushButton{background-color: rgb(186, 186, 186);}")
        self.ui.confirm_button.setStyleSheet(
            "QPushButton{background-color: rgb(187, 255, 200);}")

        cap = cv2.VideoCapture(DATA_DIR+self.fileName)
        if not cap.isOpened():
            print("Error opening a video file")
        self.frames = []
        while (cap.isOpened()):
            success, frame = cap.read()
            #print(frame_count)
            if not success:
                print("Can't read from Camera")
                break
            self.frames.append(frame)

    def upload_finished(self):
        ex = self.app.db.get_one_exercise_by_ID(self.exercise.id, session=self.session)
        self.app.add_video_card_to_banner(ex)



    def upload(self):
        self.upload_thread = ProcessingThread(self.exercise.id)
        self.upload_thread.finished.connect(self.upload_finished)
        self.upload_thread.start()
        self.app.load_page("home")




    def confirm(self):
        video_name = self.ui.video_name_editor.toPlainText()
        description = self.ui.description_editor.toPlainText()
        # tags = self.ui.tags_editor.toPlainText()
        # tag = tags.split(",")
        index = len(self.frames) // 2
        self.exercise = Exercise(
            name=video_name,
            description=description,
            video_directory=self.fileName,
            )
        self.app.db.add_exercise(self.exercise)
        self.exercise.image_directory = f"/images/{self.exercise.id}.png"
        cv2.imwrite(f"{DATA_DIR}{self.exercise.image_directory}",self.frames[index])
        self.app.db.session.commit()
        self.ui.confirm_button.setStyleSheet(
            "QPushButton{background-color: rgb(186, 186, 186);}")
        self.ui.cut_button.setStyleSheet(
            "QPushButton{background-color: rgb(187, 255, 200);}")


    def change_display_start(self):
        value = self.ui.start_slider.value()
        frame_num = round(value/100 *(len(self.frames)-1))
        frame = self.frames[frame_num]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        if self.h == None:
            self.h = h
        if self.w == None:
            self.w = w
        Qimg = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
        self.ui.video.setPixmap(QPixmap.fromImage(Qimg))

    def change_display_end(self):
        value = self.ui.end_slider.value()
        frame_num = round(value/100 *(len(self.frames)-1))
        #print(value,frame_num)
        frame = self.frames[frame_num]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        Qimg = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
        self.ui.video.setPixmap(QPixmap.fromImage(Qimg))


    def cut(self):
        self.ui.cut_button.setStyleSheet(
            "QPushButton{background-color: rgb(186, 186, 186);}")
        self.ui.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(187, 255, 200);}")
        return
        videoWriter = cv2.VideoWriter(DATA_DIR+self.fileName,cv2.VideoWriter_fourcc(*'mp4v'),30,(self.w,self.h))
        Svalue = self.ui.start_slider.value()
        Sframe_num = round(Svalue/100 *(len(self.frames)-1))
        Evalue = self.ui.end_slider.value()
        Eframe_num = round(Evalue/100 *(len(self.frames)-1))
        for index in range(len(self.frames)):
            if index > Eframe_num:
                break
            if index > Sframe_num:
                videoWriter.write(self.frames[index])
            elif index == Sframe_num:
                #print(self.exercise.image_directory)
                videoWriter.write(self.frames[index])

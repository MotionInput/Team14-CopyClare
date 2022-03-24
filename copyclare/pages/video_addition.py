import os
import sys
from tkinter import Frame
from PySide6 import QtCore, QtWidgets, QtGui

from copyclare.common import AppSingleton

from .page import Page

class Video_Addition(Page):
    def __init__(self, master):
        super().__init__(master, "video_addition")

        self.app = AppSingleton.get_app()

        # video_name = self.ui.video_name_editor.getText()
        # video_description = self.ui.description_editor.getText()
        # video_tags = self.ui.tags_editor.getText()

        self.ui.back_button.clicked.connect(lambda x: self.app.load_page("home"))
        self.ui.browse_button.clicked.connect(self.open_file)
        self.ui.upload_button.clicked.connect(self.upload)
        self.ui.confirm_button.clicked.connect(self.confirm)
        self.ui.input_area.setVisible(False)
        self.ui.video_trimmer.setVisible(False)
        self.ui.upload_button.setEnabled(False)
    
    def open_file(self):
        fileName,fileType = QtWidgets.QFileDialog.getOpenFileName(self,"Select video file",os.getcwd()+"/data/videos","video files(*.mp4)")
        self.fileName = fileName
        
        self.ui.input_area.setVisible(True)
        self.ui.video_trimmer.setVisible(True)
        
        #print(fileName)
        
    def upload(self):
        #parse the video and add a new exercise information to database
        pass

    def confirm(self):
        self.video_name = self.ui.video_name_editor.getText()
        self.video_description = self.ui.description_editor.getText()
        raw_tags = self.ui.tags_editor.getText()
        self.tags = raw_tags.split(",")

        self.ui.upload_button.setEnabled(True)
        self.ui.upload_button.setStyleSheet("Qpushbutton{background-color: rgb(85, 255, 127)}")

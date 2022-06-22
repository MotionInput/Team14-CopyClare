import time
import json

import cv2
from PySide6.QtCore import QRect, Qt, QThread, Signal
from PySide6.QtGui import QImage

from copyclare.data import DATA_DIR
from copyclare.model import AccuracyModel
from copyclare.common import AppSingleton


class ProcessingThread(QThread):
    """
    Runs the preprocessing of the video in the background once
    its created with a video addition tool
    """
    def __init__(self, exercise):
        QThread.__init__(self, None)

        self.exercise = exercise
        self.app = AppSingleton.get_app()

    def run(self):
        """
        Calls accuracy model to preprocess a video.

        """
        print("Processing", self.exercise.video_directory)
        joints = [
            "left_elbow", "left_shoulder", "right_elbow", "right_shoulder"
        ]
        accuracymodel = AccuracyModel(self.exercise, joints)
        self.exercise.angles_json = json.dumps(
            accuracymodel.get_angles(DATA_DIR + self.exercise.video_directory))
        # print(exercise.angles_json)
        print("quitting")
        self.quit()

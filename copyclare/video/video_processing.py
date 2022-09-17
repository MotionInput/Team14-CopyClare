import time
import json

import cv2
from PySide6.QtCore import QRect, Qt, QThread, Signal
from PySide6.QtGui import QImage

from copyclare.data import DATA_DIR
from copyclare.model import AccuracyModel
from copyclare.common import AppSingleton
from copyclare.data.database import Joint, ExerciseData


class ProcessingThread(QThread):
    """
    Runs the preprocessing of the video in the background once
    its created with a video addition tool
    """
    def __init__(self, exercise_id):
        QThread.__init__(self, None)

        self.app = AppSingleton.get_app()
        self.exercise_id = exercise_id

    def run(self):
        """
        Calls accuracy model to preprocess a video.

        """
        session = self.app.db.Session()
        exercise = self.app.db.get_one_exercise_by_ID(self.exercise_id, session=session)
        joints = self.app.db.get_all_joints(session=session)
        print("Processing", exercise.video_directory)
        accuracymodel = AccuracyModel(exercise, joints)
        angles = accuracymodel.get_angles(DATA_DIR + exercise.video_directory)
        for joint in joints:
            for t, angle in angles[joint.name].items():
                exercise.data.append(ExerciseData(exercise=exercise, joint=joint, time=t, angle=angle))
        print("quitting")
        session.commit()
        self.app.db.Session.remove()
        self.quit()

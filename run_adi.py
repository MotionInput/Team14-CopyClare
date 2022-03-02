import sys
import numpy as np

from PySide6.QtWidgets import QMainWindow, QApplication

from copyclare.pages import ExercisePage
from copyclare.common import load_ui
from copyclare.model import AccuracyModel
from copyclare import DATA_PATH
import matplotlib.pyplot as plt
import statsmodels.api as sm
import cv2


def test_accuracy():
    joints = {"left_shoulder", "left_elbow"}

    # am = AccuracyModel(DATA_PATH + "/videos/sample2.mp4", joints)

    cap = cv2.VideoCapture(2)

    print("initialised, starting camera")

    while cap.isOpened():
        success, img = cap.read()

        cv2.imshow("Image", img)
        if not success:
            print("can't ")
            break


def test_ui():

    app = QApplication(sys.argv)
    window = QMainWindow()
    window.showMaximized()
    ui = load_ui("main_window")
    ui.setupUi(window)
    ex = ExercisePage(window)
    ui.pages_layout.addWidget(ex)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    from copyclare.model import Database



    # accuracy = am.accuracy(frame)
    # print(accuracy)

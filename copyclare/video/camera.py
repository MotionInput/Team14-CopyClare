"""
Contributors: Adi Bozzhanov

"""
import json
import time

import cv2
from PySide6.QtCore import QRect, Qt, QThread, Signal, Slot
from PySide6.QtGui import QImage
import numpy as np
from scipy.signal import savgol_filter, find_peaks

from copyclare.data import DATA_DIR
from copyclare.model import AccuracyModel
from copyclare.elbow.PoseModule import poseDetector
from copyclare.common import AppSingleton


WINDOW = 21
ORDER = 3
FRAME_BUFFER = 5

def find_zero_grad(grad, start, direction):
    grad_slice = grad[start::direction]
    for i, d in enumerate(grad_slice):
        if d * grad_slice[i + 1] <= 0:
            return start + direction * i


def find_prominent_joint(exercise_angles, joints_map):
    max_prominence = 0
    prom_joint = None
    peak_type = None
    peak_position = None
    base = None
    for joint in joints_map.keys():
        data = savgol_filter(np.fromiter(exercise_angles[joint].values(), float), WINDOW, ORDER)
        for direction in [1, -1]:
            peak_positions, props = find_peaks(direction * data, prominence=0)
            for i, peak in enumerate(peak_positions):
                if props["prominences"][i] > max_prominence:
                    max_prominence = props["prominences"][i]
                    prom_joint = joint
                    peak_type = direction
                    peak_position = peak
                    base = (data[props["left_bases"][i]] + data[props["right_bases"][i]]) / 2
    return max_prominence, prom_joint, peak_type, peak_position, base


def find_extreme_grad(angles, t, minimum=False):
    if minimum:
        d = -1
    else:
        d = 1
    grad = np.gradient(angles, t)
    positions, props = find_peaks(d * grad, prominence=0)
    max_prom = 0
    pos = None
    for i, prom in enumerate(props["prominences"]):
        if prom > max_prom:
            max_prom = prom
            pos = positions[i]
    return pos

def find_slice(angles, t):
    min_pos = find_extreme_grad(angles, t, minimum=True)
    max_pos = find_extreme_grad(angles, t, minimum=False)
    grad = np.gradient(angles, t)
    beginning = find_zero_grad(grad, min(min_pos, max_pos), -1)
    end = find_zero_grad(grad, max(min_pos, max_pos), 1)
    return slice(beginning, end)


class CameraThread(QThread):
    """
    Class responsible for updating the Exercise page with
    camera_feed, accuracy_graph and a repetition count.
    """

    update_frame = Signal(QImage)
    update_reps = Signal(int)
    update_graph = Signal(list)
    update_progress = Signal(int)

    def __init__(self, container, exercise_id):
        QThread.__init__(self, None)
        self.app = AppSingleton.get_app()
        self.session = self.app.db.Session()
        exercise = self.app.db.get_one_exercise_by_ID(exercise_id, session=self.session)
        self.joints_map = self.app.db.get_joints_map(session=self.session)
        self.container = container
        self._running = True
        self.worker = CameraWorker(exercise, self.joints_map)
        self.reps = 0

    def toggle_flipped(self):
        self.worker.flip = not(self.worker.flip)

    def run(self):
        """
        Threads main run method

        Invokes the camera worker and processes every frame of it to
        update the ui.

        emmits ``update_frame``, ``update_reps`` and ``update_graph`` signals

        """
        count = 0

        for frame in self.worker.work():
            count += 1
            if not self._running:
                break

            _, _, width, height = self.container.frameGeometry().getRect()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            self.update_reps.emit(self.worker.num_of_repetitions)

            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)

            scaled_img = img.scaled(width, height,
                                    Qt.KeepAspectRatioByExpanding)

            self.update_frame.emit(scaled_img)
            self.update_progress.emit(int(self.worker.per))

        self.worker.cap.release()
        self.app.db.Session.remove()
        self.quit()


class CameraWorker:
    """
    Camera worker that can ignore ui and threading logic and process just
    data.


    """
    def __init__(self, exercise, joints_map):

        self.exercise = exercise
        self.threshold = 0.5
        
        self.cap = None
        # self.model = AccuracyModel(exercise, joints)
        angles = exercise.get_angles()
        self.joints_map = joints_map
        max_prominence, prom_joint, peak_type, peak_position, base = find_prominent_joint(angles, self.joints_map)
        self.stored_time = np.fromiter(angles[prom_joint].keys(), float)
        self.prom_angles = savgol_filter(np.fromiter(angles[prom_joint].values(), float), WINDOW, ORDER)
        self.joint = prom_joint
        self.max_prominence = max_prominence
        self.peak_type = peak_type
        self.peak_position = peak_position
        self.base = base
        self.flip = False

        interest = find_slice(self.prom_angles, self.stored_time)
        self.detector = poseDetector()

    def work(self):
        """
        Generator that yields processed
        frames and accesses AccuracyModel

        """

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while not self.cap.isOpened():
            print("Error opening a video file in camera, trying default api")
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("Error opening camera")

        self.beginning = time.time()
        self.accuracy = 0
        self.num_of_repetitions = 0
        self.updated = False
        self.accuracy_vals = []
        self.angle_stream = []
        self.time_stream = []
        self.per = 0

        start = time.time()
        while (self.cap.isOpened()):
            success, frame = self.cap.read()
            if not success:
                print("Can't read from Camera")
                continue
            frame = cv2.flip(frame, 180)
            frame = self.detector.findPose(frame, False)
            lmList = self.detector.findPosition(frame, False)

            if self.flip:
                if "left" in self.joint:
                    joint = self.joint.replace("left", "right")
                else:
                    joint = self.joint.replace("right", "left")
            else:
                joint = self.joint

            if len(lmList) != 0:
                angle = self.detector.findAngle(frame, *self.joints_map[joint])
                self.angle_stream.append(angle)

                self.per = np.interp(angle, sorted((self.max_prominence, self.base)), (0, 100)[::self.peak_type])
                color = (0, 255, 0)
                if len(self.angle_stream) % FRAME_BUFFER == 0:
                    data = savgol_filter(np.fromiter(self.angle_stream, float), FRAME_BUFFER, ORDER)
                    peak_positions, props = find_peaks(self.peak_type * data, prominence=self.threshold * self.max_prominence)
                    if peak_positions:
                        self.num_of_repetitions += 1
                        prom_angle = self.angle_stream[peak_positions[0]]
                        self.accuracy_vals.append((time.time() - start, np.interp(prom_angle, (self.max_prominence, self.base), (100, 0))))
                        self.angle_stream = self.angle_stream[props["right_bases"][0]:]

            # frame = cv2.flip(frame, 1)

            yield frame

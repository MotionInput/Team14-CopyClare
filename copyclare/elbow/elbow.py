import cv2
import numpy as np
from copyclare.elbow import PoseModule as pm
from copyclare.model.accuracy_v2 import AccuracyModel
from copyclare.data.database import Database
from copyclare.data import DB_DIR
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks
import json
import time

WINDOW = 21
ORDER = 3
FRAME_BUFFER = 5

joints_map = {
    "left_elbow": (15, 13, 11),
    "right_elbow": (12, 14, 16),
    "left_shoulder": (13, 11, 12),
    "right_shoulder": (11, 12, 14),
}


def find_zero_grad(grad, start, direction):
    grad_slice = grad[start::direction]
    for i, d in enumerate(grad_slice):
        if d * grad_slice[i + 1] <= 0:
            return start + direction * i


def find_prominent_joint(exercise_angles):
    max_prominence = 0
    prom_joint = None
    peak_type = None
    peak_position = None
    base = None
    for joint in joints_map.keys():
        data = savgol_filter(np.fromiter(angles[joint].values(), float), WINDOW, ORDER)
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


d = Database(DB_DIR)
e = d.get_all_exercises()[0]
angles = json.loads(e.angles_json)
t = np.fromiter(angles["left_shoulder"].keys(), float)

prominence, joint, direction, position, base = find_prominent_joint(angles)
data = savgol_filter(np.fromiter(angles[joint].values(), float), WINDOW, ORDER)
interest = find_slice(data, t)

def run():
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        detector = pm.poseDetector()
        count = 0
        dir = 0
        angle_stream = []

        while True:
            success, img = cap.read()
            img = cv2.flip(img, 180)
            # img = cv2.imread("AITrainer/try.jpg")
            img = cv2.resize(img, (960, 560))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            # print(lmList)
            if len(lmList) != 0:
                # Right arm since flip
                # angle = detector.findAngle(img, 11, 13, 15)
                # Left arm
                angle = detector.findAngle(img, *joints_map[joint])
                angle_stream.append(angle)

                per = np.interp(angle, (prominence, base), (100,0))
                bar = np.interp(angle, (prominence, base), (100, 650))

                color = (0, 255, 0)
                if len(angle_stream) % FRAME_BUFFER == 0:
                    data = savgol_filter(np.fromiter(angle_stream, float), FRAME_BUFFER, ORDER)
                    #data = angle_stream
                    peak_positions, props = find_peaks(direction * data, prominence=0.5 * prominence)
                    if peak_positions:
                        print(peak_positions, props)
                        count += 1
                        angle_stream = angle_stream[props["right_bases"][0]:]

                # print(count)

                cv2.rectangle(img, (0, 340), (210, 600), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (35, 500), cv2.FONT_HERSHEY_PLAIN, 8,
                            (255, 0, 0), 15)

                cv2.rectangle(img, (770, 100), (800, 560), color, 3)
                cv2.rectangle(img, (770, int(bar)), (800, 560), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)} %', (730, 70), cv2.FONT_HERSHEY_PLAIN, 4,
                            color, 4)
    
            cv2.imshow("Image", img)
            cv2.waitKey(100)
    finally:
        cap.release()
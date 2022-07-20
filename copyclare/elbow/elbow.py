import cv2
import numpy as np
import PoseModule as pm

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = pm.poseDetector()
count = 0
dir = 0

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
        angle = detector.findAngle(img, 12, 14,16)
        
        per = np.interp(angle, (77,169), (0,100))
        bar = np.interp(angle, (77,169), (650, 100))

        color = (0, 255, 0)

        if per >= 91:
            if dir == 0:
                count += 0.5
                dir = 1
        if per <= 5:
            if dir == 1:
                count += 0.5
                dir = 0
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
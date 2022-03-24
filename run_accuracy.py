from copyclare.model import AccuracyModel
from copyclare import DATA_PATH
from copyclare.model import Database
from copyclare.model.database import DB_DIR
import cv2

if __name__ == "__main__":
    joints = ["left_elbow", "left_shoulder", "right_elbow", "right_shoulder"]
    db = Database(DB_DIR)
    exercises = db.get_all_exercises()
    for ex in exercises:
        ex.angles_json = "null"
        a = AccuracyModel(ex,joints)
        vidcap = cv2.VideoCapture(DATA_PATH + ex.video_directory)
        success, image = vidcap.read()
        print(success)
        if success:
            cv2.imwrite(f"{DATA_PATH}/test/{ex.id}.png", image)

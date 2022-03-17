from copyclare.model import AccuracyModel
from copyclare import DATA_PATH
from copyclare.model import Database
from copyclare.model.database import DB_DIR

if __name__ == "__main__":
    joints = ["left_elbow", "left_shoulder"]
    db = Database(DB_DIR)
    exercises = db.get_all_exercises()
    for ex in exercises:
        ex.angles_json = "null"
        a = AccuracyModel(ex,joints)

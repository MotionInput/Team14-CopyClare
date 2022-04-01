import time
import json

from copyclare.model import AccuracyModel
from copyclare.data.objects import Exercise


def test(case, joints):

    test_path = f"test_data/{case}.mp4"
    mock_ex = Exercise(1, 1, 1, 1, 1, "-1")
    am = AccuracyModel(mock_ex, joints)
    start = time.time()
    am.get_angles(test_path)
    return time.time() - start


joints = ["left_elbow", "right_elbow", "left_shoulder", "right_shoulder"]

data = {
    1: [],
    2: [],
    3: [],
}

for i in range(3):
    test_joints = joints[:i + 1]

    for j in range(2, 16):
        res = test(j, test_joints)
        data[i + 1].append(res)

results = json.dumps(data, indent=4)

with open("test_results.json", "w") as f:
    f.write(results)

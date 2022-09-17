import shutil
import cv2
import pathlib
import re
import os
import mediapipe
from distutils.dir_util import copy_tree

cv2dir = pathlib.Path(cv2.__file__).parent

for file in os.listdir(cv2dir):
    if re.search(r"config*.py", file):
        print(f"Copying {file} to cv2 directory")
        shutil.copyfile(cv2dir.joinpath(file), f"build/copyclare/run.app/cv2/{file}")

mediapipedir = pathlib.Path(mediapipe.__file__).parent

copy_tree(mediapipedir.joinpath("modules"), "build/copyclare/run.app/mediapipe/modules")
import shutil
import cv2
import pathlib
import re
import os

cv2dir = pathlib.Path(cv2.__file__).parent

for file in os.listdir(cv2dir):
    if re.search(r"config*.py", file):
        print(f"Copying {file} to cv2 directory")
        shutil.copyfile(cv2dir.joinpath(file), f"build/copyclare/run.app/cv2/{file}")
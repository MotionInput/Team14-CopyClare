import os
import pathlib
import mediapipe
import subprocess

dir_path = pathlib.Path(mediapipe.__file__).parent.joinpath('python')
so_name = [f for f in os.listdir(dir_path) if f.split('.')[-1] == 'so'][0]
so_path = str(dir_path.joinpath(so_name))
subprocess.call(f"install_name_tool -id {so_path} {so_path}", shell=True)
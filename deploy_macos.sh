python update_mediapipe_so.py
python -m nuitka --standalone --lto=no --assume-yes-for-downloads --plugin-enable=numpy --plugin-enable=pyside6 --output-dir=build/copyclare run.py

rm -r build/copyclare/run.app
mv build/copyclare/run.dist build/copyclare/run.app
mkdir build/copyclare/run.app/data
cp -r  data_clean/* build/copyclare/run.app/data
python copycv2configs.py
python update_mediapipe_so.py
python -m nuitka --standalone --lto=no --assume-yes-for-downloads --plugin-enable=numpy --plugin-enable=pyside6 --disable-plugin=anti-bloat --output-dir=build/copyclare run.py

mkdir build/copyclare/run.dist/data
cp -r  data_clean/* build/copyclare/run.dist/data
mv build/copyclare/run.dist /build/copyclare/run.app

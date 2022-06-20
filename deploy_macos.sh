python update_mediapipe_so.py
python -m nuitka --standalone --lto=no --assume-yes-for-downloads --plugin-enable=numpy --plugin-enable=pyside6 --disable-plugin=anti-bloat --include-module=numpy.core.multiarray --output-dir=build/copyclare run.py

mv build/copyclare/run.dist build/copyclare/run.app
mkdir build/copyclare/run.dist/data
cp -r  data_clean/* build/copyclare/run.dist/data

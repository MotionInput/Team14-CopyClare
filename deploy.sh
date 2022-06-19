
python --version

python -m nuitka --lto=no --assume-yes-for-downloads --plugin-enable=numpy --plugin-enable=pyide6 --output-dir=build/copyclare run.py

mkdir build/copclare/run.dist/data
cp -r  data_clean/* build/copyclare/run.dist/data

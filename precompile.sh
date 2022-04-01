mkdir copyclare/pyui

for f in ./copyclare/ui/*
do
    NAME="$(basename $f .ui)"
    echo "Compiling: $NAME"
    pyside6-uic $f -o ./copyclare/pyui/"$NAME".py
done

echo "Compiling: res.qrc"
pyside6-rcc res.qrc -o res_rc.py

if [ -d "./data" ]
then
    echo "Data exists. Nothing to do."
else
    echo "Data does no exist. Initialising from data_clean"
    mkdir data
    mkdir data/progress-charts
    mkdir data/accuracy-graphs
    cp -r data_clean/* data

fi

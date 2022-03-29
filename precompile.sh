for f in ./copyclare/ui/*
do
    NAME="$(basename $f .ui)"
    echo "Compiling: $NAME"
    pyside6-uic $f -o ./copyclare/pyui/"$NAME".py
done

echo "Compiling: res.qrc"
pyside6-rcc res.qrc -o res_rc.py

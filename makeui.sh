for f in ./copyclare/ui/*
do
    NAME="$(basename $f .ui)"
    echo "Compiling: $NAME"
    pyside6-uic $f -o ./copyclare/pyui/"$NAME".py
done

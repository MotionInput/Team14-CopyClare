for f in ./*
do
    NAME="$(basename $f .ui)"
    echo "Compiling: $NAME"
    pyside6-uic $f -o compiled/"$NAME".py
done
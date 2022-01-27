import os

from PySide6.QtUiTools import loadUiType


def load_ui(fname):
    path = os.path.dirname(__file__)
    ui, _ = loadUiType(f"{path}/views/ui/{fname}.ui")
    return ui()

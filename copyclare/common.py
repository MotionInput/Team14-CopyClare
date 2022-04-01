"""
Contributors: Adi Bozzhanov

"""

import os

from PySide6.QtUiTools import loadUiType


def load_ui(fname):
    """Loads the UI file and returns the UI object.

    Args:
        fname (str)): name of the UI element

    Returns:
        object: this is the object degenerated from UI
    """
    print(f"DEBUG: Compiling: {fname}")
    path = os.path.dirname(__file__)
    ui, _ = loadUiType(f"{path}/ui/{fname}.ui")
    return ui()


class AppSingleton:

    _app = None

    @classmethod
    def get_app(cls):
        from copyclare import App
        if cls._app is None:
            cls._app = App()
        return cls._app

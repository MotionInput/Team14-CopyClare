import os

from PySide6.QtUiTools import loadUiType


def load_ui(fname):
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

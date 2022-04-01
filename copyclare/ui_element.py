"""
Contributors: Adi Bozzhanov

"""

from PySide6.QtWidgets import QFrame

from copyclare.config import DEBUG
from copyclare.common import load_ui


class UiElement(QFrame):
    """This class just calls UI differently based on debug mode

    Args:
        master: The parent widget
        page_ui: The UI file to load
        compiled_ui: The compiled UI function
    """

    def __init__(self, master, page_ui, compiled_ui):
        super().__init__(master)

        if DEBUG:
            self.ui = load_ui(page_ui)
        else:
            self.ui = compiled_ui()

        self.ui.setupUi(self)

import os

from PySide6.QtWidgets import QFrame

from common import load_ui


class Page(QFrame):
    def __init__(self, master, page_ui):
        super().__init__(master)

        self.ui = load_ui(page_ui)
        self.ui.setupUi(self)

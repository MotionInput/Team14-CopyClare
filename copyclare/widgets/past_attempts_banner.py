from PySide6.QtWidgets import QFrame

from copyclare.common import load_ui
from copyclare.pyui.past_attempts_banner import Ui_Frame
from copyclare import UiElement


class PastAttemptsBannerWidget(UiElement):
    def __init__(self, master):
        super().__init__(master, "past_attempts_banner", Ui_Frame)


        self.ui.export_all_button.clicked.connect(lambda x: self._export_all())

    # TODO - link export_all function here
    def _export_all(self):
        print("export all")

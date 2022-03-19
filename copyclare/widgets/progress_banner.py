from PySide6.QtWidgets import QFrame

from copyclare.widgets import VideoCardWidget
from copyclare.common import load_ui


class ProgressBannerWidget(QFrame):
    def __init__(self, master):
        super().__init__(master)
        self.ui = load_ui("progress_banner")
        self.ui.setupUi(self)

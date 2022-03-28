from PySide6.QtWidgets import QFrame

from copyclare.common import load_ui
from copyclare.widgets import VideoCardWidget


class ProgressBannerWidget(QFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.ui = load_ui("progress_banner")
        self.ui.setupUi(self)
        self.ui.category_title.setText(title)

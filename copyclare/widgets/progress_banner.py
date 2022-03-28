from PySide6.QtWidgets import QFrame

from copyclare.common import load_ui
from copyclare.widgets import VideoCardWidget
from copyclare.pyui.progress_banner import Ui_Frame
from copyclare import UiElement



class ProgressBannerWidget(UiElement):
    def __init__(self, master, title):
        super().__init__(master, "progress_banner", Ui_Frame)
        self.ui.category_title.setText(title)

"""
Contributors: Adi Bozzhanov, Yan Lai

"""

from copyclare.pyui.progress_banner import Ui_Frame
from copyclare import UiElement


class ProgressBannerWidget(UiElement):
    def __init__(self, master, title):
        super().__init__(master, "progress_banner", Ui_Frame)
        self.ui.category_title.setText(title)

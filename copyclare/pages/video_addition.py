from PySide6.QtCore import Qt

from copyclare.widgets.progress_banner import ProgressBannerWidget

from .page import Page


class Video_Addition(Page):
    def __init__(self, master):
        super().__init__(master, "ADD VIDEO")
        
        _banner = ProgressBannerWidget(self)
        self.ui.verticalLayout.insertWidget(0, _banner)

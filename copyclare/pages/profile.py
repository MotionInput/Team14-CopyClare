from copyclare.widgets.banner import BannerWidget
from PySide6.QtCore import Qt

from .page import Page


class ProfilePage(Page):
    def __init__(self, master):
        super().__init__(master, "profile")
        
        _banner = BannerWidget(self, "Progress")
        _banner.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        _banner.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.verticalLayout.insertWidget(0, _banner)



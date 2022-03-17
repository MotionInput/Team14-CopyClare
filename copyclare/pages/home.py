from copyclare.model import Database
from copyclare.widgets import BannerWidget
from copyclare.common import AppSingleton

from .page import Page


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, "home")

        self.app = AppSingleton.get_app()

        tags = self.app.db.get_all_tags()

        for tag in tags:
            _banner = BannerWidget(self.ui.scroll_area, tag.tag_name)
            self.ui.vertical_layout.addWidget(_banner)

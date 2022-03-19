from copyclare.model import Database
from copyclare.widgets import BannerWidget
from copyclare.common import AppSingleton

from .page import Page


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, "home")

        self.app = AppSingleton.get_app()


        all_exercises = self.app.db.get_all_exercises()
        library_banner = BannerWidget(self.ui.scroll_area, "Library", all_exercises)
        self.ui.vertical_layout.insertWidget(0, library_banner)

        tags = self.app.db.get_all_tags()
        for tag in tags:
            exercises = self.app.db.get_exercises_by_tag(tag)
            _banner = BannerWidget(self.ui.scroll_area, tag.tag_name,
                                   exercises)
            self.ui.vertical_layout.insertWidget(0, _banner)

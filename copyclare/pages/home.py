from copyclare.common import AppSingleton
from copyclare.data import Database
from copyclare.widgets import BannerWidget
from copyclare.pyui.home import Ui_Home

from copyclare import UiElement


class HomePage(UiElement):
    def __init__(self, master):
        super().__init__(master, "home", Ui_Home)

        self.app = AppSingleton.get_app()
        self.banners = {}

        all_exercises = self.app.db.get_all_exercises()
        library_banner = BannerWidget(self.ui.scroll_area, "Exercise Library",
                                      all_exercises)
        self.ui.vertical_layout.insertWidget(0, library_banner)

        tags = self.app.db.get_all_tags()
        for tag in tags:
            exercises = self.app.db.get_exercises_by_tag(tag)
            self.banners[tag.tag_name] = BannerWidget(self.ui.scroll_area,
                                                      tag.tag_name, exercises)
            self.ui.vertical_layout.insertWidget(0, self.banners[tag.tag_name])

from copyclare.common import AppSingleton
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
                                      all_exercises, False)
        self.ui.vertical_layout.insertWidget(0, library_banner)

        # TODO - if tag.tag_name == "My Exercises", set to True (remove state)
        tags = self.app.db.get_all_tags()
        for tag in tags:
            if tag.tag_name == "My Exercises":
                remove_state = True
            else:
                remove_state = False
            exercises = self.app.db.get_exercises_by_tag(tag)
            self.banners[tag.tag_name] = BannerWidget(self.ui.scroll_area,
                                                      tag.tag_name, exercises, remove_state)
            self.ui.vertical_layout.insertWidget(0, self.banners[tag.tag_name])

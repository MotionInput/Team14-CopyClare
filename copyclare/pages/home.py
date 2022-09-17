"""
Contributors: Adi Bozzhanov

"""

from copyclare.common import AppSingleton
from copyclare.widgets import BannerWidget
from copyclare.pyui.home import Ui_Home

from copyclare import UiElement


class HomePage(UiElement):
    """
    Initialise the home page.

    Creates banners (which displays video cards) for all tags.
    One banner for each tag.

    Args:
        master (ParentWidget): The frame in which the page will be displayed in.

    """

    def __init__(self, master):
        super().__init__(master, "home", Ui_Home)

        self.app = AppSingleton.get_app()
        self.banners = {}
        all_exercises = self.app.db.get_all_exercises()
        self.banners["Exercise Library"] = BannerWidget(self.ui.scroll_area, "Exercise Library",
                                      all_exercises)
        self.ui.vertical_layout.insertWidget(0, self.banners["Exercise Library"])

        tags = self.app.db.get_all_tags()
        for tag in tags:
            exercises = self.app.db.get_exercises_by_tag(tag)
            self.banners[tag.name] = BannerWidget(self.ui.scroll_area,
                                                      tag.name, exercises)
            self.ui.vertical_layout.insertWidget(0, self.banners[tag.name])

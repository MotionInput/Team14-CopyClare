from copyclare.widgets import BannerWidget

from .page import Page


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, "home")

        categories = ["Today", "Library"]

        for title in categories:
            _banner = BannerWidget(self.ui.scroll_area, title)
            self.ui.vertical_layout.insertWidget(0, _banner)

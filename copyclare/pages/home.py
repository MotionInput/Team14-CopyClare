from copyclare.model import Database
from copyclare.widgets import BannerWidget
from copyclare.common import AppSingleton

from .page import Page


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, "home")

        self.app = AppSingleton.get_app()
        print(self.app)

        tags = self.app.db.get_all_categories()

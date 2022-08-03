from copyclare.pyui.plan import Ui_planning

from copyclare import UiElement
from copyclare.common import AppSingleton


class PlanPage(UiElement):

    def __init__(self, master):
        super().__init__(master, "planning", Ui_planning)
        self.app = AppSingleton.get_app()

        self.ui.pushButton.clicked.connect(
            lambda x: self.app.load_page("home"))
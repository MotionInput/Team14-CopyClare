"""
Contributors: Yan Lai

"""

from copyclare.pyui.landing import Ui_landing_frame
from copyclare.common import AppSingleton
from copyclare.widgets.tutorial_popup import TutorialPopupWidget
from copyclare import UiElement


class LandingPage(UiElement):
    def __init__(self, master):
        super().__init__(master, "landing", Ui_landing_frame)

        self.app = AppSingleton.get_app()

        self.ui.start_btn.clicked.connect(
            lambda x: self._load_home_page())
    
    def _load_home_page(self):
        self.app.ui.side_nav.show()
        tutorial_popup = TutorialPopupWidget()
        tutorial_popup.show()
        self.app.load_page("home")

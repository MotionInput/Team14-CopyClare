from copyclare.pyui.not_found import Ui_not_found

from copyclare import UiElement


class NotFound(UiElement):
    def __init__(self, master):
        super().__init__(master, "not_found", Ui_not_found)

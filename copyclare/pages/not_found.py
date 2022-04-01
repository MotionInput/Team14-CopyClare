"""
Contributors: Adi Bozzhanov

"""

from copyclare.pyui.not_found import Ui_not_found

from copyclare import UiElement


class NotFound(UiElement):
    """
    Initialise the 'not found' page. This is displayed 
    if a page that does not exist is called to be loaded.

    Args:
        master (ParentWidget): The frame in which the page will be displayed in.

    """

    def __init__(self, master):
        super().__init__(master, "not_found", Ui_not_found)

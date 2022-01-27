"""
Main code runner
"""
from views import View


class Controller:
    """
    Controlls cross module interaction
    """

    def __init__(self):
        self.view = View()

    def start_app(self):
        self.view.start_ui()

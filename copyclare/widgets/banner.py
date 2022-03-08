from PySide6.QtWidgets import QFrame



from copyclare.common import load_ui


class BannerWidget(QFrame):

    def __init__(self, master, banner_name):
        super().__init__(master)
        self.ui = load_ui("banner")
        self.ui.setupUi(self)

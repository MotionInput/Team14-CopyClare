from PySide6.QtWidgets import QFrame

from copyclare.common import load_ui


class PastAttemptsBannerWidget(QFrame):
    def __init__(self, master):
        super().__init__(master)
        self.ui = load_ui("past_attempts_banner")
        self.ui.setupUi(self)

        self.ui.export_all_button.clicked.connect(
            lambda x: self._export_all())

    # TODO - link export_all function here
    def _export_all(self):
        print("export all")

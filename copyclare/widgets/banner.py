from PySide6.QtWidgets import QFrame

from copyclare.widgets import VideoCardWidget
from copyclare.common import load_ui


class BannerWidget(QFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.ui = load_ui("banner")
        self.ui.setupUi(self)
        self.ui.category_title.setText(title)

        for i in range(10):
            title, description, duration, img_path = map(
                str, (i, i + 1, i + 2, i + 4))
            _card = VideoCardWidget(self.ui.scrollArea, title, description,
                                    duration, img_path)
            self.ui.horizontalLayout.addWidget(_card)

from PySide6.QtWidgets import QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from copyclare import DATA_PATH
from copyclare.common import load_ui


class TutorialPopupWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("tutorial_popup")
        self.ui.setupUi(self)

        self.tutorial_page = 0

        self.tutorial_texts = [
            ("Home Page:", "Click on a video card to get started.",
             "/assets/tutorial-home.png"),
            ("Exercise Page:",
             "Press 'End exercise' button to stop exercise & store attempt.",
             "/assets/tutorial-ex.jpg"),
            ("Profile Page:",
             "Check your progess and all past attempts here. Export function available.",
             "/assets/tutorial-profile.jpg")
        ]

        self.ui.prev_button.clicked.connect(lambda x: self.load_prev())
        self.ui.next_button.clicked.connect(lambda x: self.load_next())

        self._load_texts()

    def load_prev(self):
        if self.tutorial_page != 0:
            self.tutorial_page -= 1
            self._load_texts()

    def load_next(self):
        if self.tutorial_page != (len(self.tutorial_texts) - 1):
            self.tutorial_page += 1
            self._load_texts()

    def _load_texts(self):
        self.ui.name.setText(self.tutorial_texts[self.tutorial_page][0])
        self.ui.desc.setText(self.tutorial_texts[self.tutorial_page][1])
        pixmap = QPixmap(DATA_PATH +
                         self.tutorial_texts[self.tutorial_page][2])
        pixmap = pixmap.scaled(700, 500, Qt.KeepAspectRatio)
        self.ui.image.setPixmap(pixmap)

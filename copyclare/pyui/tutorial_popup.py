# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tutorial_popup.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Tutorial(object):
    def setupUi(self, Tutorial):
        if not Tutorial.objectName():
            Tutorial.setObjectName(u"Tutorial")
        Tutorial.resize(606, 300)
        Tutorial.setMaximumSize(QSize(16777215, 16777215))
        Tutorial.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;")
        Tutorial.setFrameShape(QFrame.StyledPanel)
        Tutorial.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(Tutorial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name = QLabel(Tutorial)
        self.name.setObjectName(u"name")
        self.name.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setBold(True)
        self.name.setFont(font)
        self.name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name)

        self.frame_2 = QFrame(Tutorial)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.desc = QLabel(self.frame_2)
        self.desc.setObjectName(u"desc")
        self.desc.setMaximumSize(QSize(16777215, 60))
        self.desc.setStyleSheet(u"padding-bottom: 10px;")

        self.verticalLayout_2.addWidget(self.desc)

        self.image = QLabel(self.frame_2)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.image)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Tutorial)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prev_button = QPushButton(self.frame)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setFont(font)
        self.prev_button.setStyleSheet(u"background-color: #90b6d6;")

        self.horizontalLayout.addWidget(self.prev_button)

        self.next_button = QPushButton(self.frame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setFont(font)
        self.next_button.setStyleSheet(u"background-color: rgb(102, 204, 255);")

        self.horizontalLayout.addWidget(self.next_button)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Tutorial)

        QMetaObject.connectSlotsByName(Tutorial)
    # setupUi

    def retranslateUi(self, Tutorial):
        Tutorial.setWindowTitle(QCoreApplication.translate("Tutorial", u"Frame", None))
        self.name.setText(QCoreApplication.translate("Tutorial", u"Page name", None))
        self.desc.setText(QCoreApplication.translate("Tutorial", u"Page description", None))
        self.image.setText(QCoreApplication.translate("Tutorial", u"image here", None))
        self.prev_button.setText(QCoreApplication.translate("Tutorial", u"Previous", None))
        self.next_button.setText(QCoreApplication.translate("Tutorial", u"Next", None))
    # retranslateUi


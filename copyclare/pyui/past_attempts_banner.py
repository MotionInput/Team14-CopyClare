# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'past_attempts_banner.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(782, 548)
        Frame.setFrameShape(QFrame.NoFrame)
        Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setStyleSheet(u"background-color: #35638e;\n"
"padding-left: 2px;\n"
"padding-right: 15px;\n"
"font-size: 30px;\n"
"color: #ffffff;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.export_all_button = QPushButton(self.frame)
        self.export_all_button.setObjectName(u"export_all_button")
        self.export_all_button.setMinimumSize(QSize(100, 50))
        self.export_all_button.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setBold(True)
        self.export_all_button.setFont(font)
        self.export_all_button.setStyleSheet(u"background-color: rgb(209, 244, 255);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-right: 0px;")

        self.horizontalLayout.addWidget(self.export_all_button)


        self.verticalLayout.addWidget(self.frame)

        self.scrollArea = QScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 400))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 758, 428))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 400, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Past attempts", None))
        self.export_all_button.setText(QCoreApplication.translate("Frame", u"Export all", None))
    # retranslateUi


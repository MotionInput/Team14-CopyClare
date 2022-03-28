# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_banner.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QScrollArea,
                               QSizePolicy, QVBoxLayout, QWidget)


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(782, 548)
        Frame.setFrameShape(QFrame.NoFrame)
        Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.category_title = QLabel(Frame)
        self.category_title.setObjectName(u"category_title")
        self.category_title.setMinimumSize(QSize(0, 80))
        font = QFont()
        self.category_title.setFont(font)
        self.category_title.setStyleSheet(u"background-color: #955fff;\n"
                                          "padding: 15px;\n"
                                          "font-size: 30px;\n"
                                          "color: #ffffff;")

        self.verticalLayout.addWidget(self.category_title)

        self.scrollArea = QScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 758, 436))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(
            QCoreApplication.translate("Frame", u"Frame", None))
        self.category_title.setText(
            QCoreApplication.translate("Frame", u"Progress", None))

    # retranslateUi

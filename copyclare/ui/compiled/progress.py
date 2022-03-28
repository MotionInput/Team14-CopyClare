# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime,
                            QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLabel, QLayout, QPushButton, QScrollArea,
                               QSizePolicy, QVBoxLayout, QWidget)


class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(933, 869)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
        Home.setMinimumSize(QSize(933, 717))
        Home.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(Home)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16777215, 100))
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.title_frame)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel{\n" "	color: #000000;\n" "\n" "}")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.verticalLayout.addWidget(self.title_frame)

        self._frame = QFrame(Home)
        self._frame.setObjectName(u"_frame")
        self._frame.setFrameShape(QFrame.NoFrame)
        self._frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self._frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self._frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.header_frame = QFrame(self.content_frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.header = QLabel(self.header_frame)
        self.header.setObjectName(u"header")

        self.horizontalLayout_3.addWidget(self.header)

        self.export_button = QPushButton(self.header_frame)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.export_button)

        self.verticalLayout_4.addWidget(self.header_frame)

        self.dropdown_frame = QHBoxLayout()
        self.dropdown_frame.setObjectName(u"dropdown_frame")
        self.exercise_dropdown = QComboBox(self.content_frame)
        self.exercise_dropdown.setObjectName(u"exercise_dropdown")

        self.dropdown_frame.addWidget(self.exercise_dropdown)

        self.date_dropdown = QComboBox(self.content_frame)
        self.date_dropdown.setObjectName(u"date_dropdown")
        self.date_dropdown.setMaximumSize(QSize(300, 16777215))

        self.dropdown_frame.addWidget(self.date_dropdown)

        self.verticalLayout_4.addLayout(self.dropdown_frame)

        self.scrollArea = QScrollArea(self.content_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 917, 654))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout_2.addWidget(self.content_frame)

        self.verticalLayout.addWidget(self._frame)

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)

    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.title.setText(
            QCoreApplication.translate("Home", u"Progress", None))
        self.header.setText(
            QCoreApplication.translate("Home", u"History", None))
        self.export_button.setText(
            QCoreApplication.translate("Home", u"Export All", None))

    # retranslateUi

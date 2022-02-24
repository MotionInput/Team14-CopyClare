# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(721, 452)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
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
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: #000000;\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.title_frame)

        self._frame = QFrame(Home)
        self._frame.setObjectName(u"_frame")
        self._frame.setFrameShape(QFrame.NoFrame)
        self._frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self._frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.general_frame = QFrame(self._frame)
        self.general_frame.setObjectName(u"general_frame")
        self.general_frame.setMinimumSize(QSize(0, 140))
        self.general_frame.setMaximumSize(QSize(16777215, 140))
        self.general_frame.setStyleSheet(u"QFrame{\n"
"	background-color: #c8c8c8;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: #ced4da;\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 10;\n"
"	max-width: 120;\n"
"	min-width: 120;\n"
"	height: 120;\n"
"	margin-left: 10;\n"
"	margin-right: 10;\n"
"	margin-top: 5;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #adb5bd;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #dee2e6;\n"
"}")
        self.general_frame.setFrameShape(QFrame.NoFrame)
        self.general_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.general_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.latest_button = QPushButton(self.general_frame)
        self.latest_button.setObjectName(u"latest_button")

        self.horizontalLayout_2.addWidget(self.latest_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.groups_button = QPushButton(self.general_frame)
        self.groups_button.setObjectName(u"groups_button")

        self.horizontalLayout_2.addWidget(self.groups_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.general_frame)

        self.content_frame = QFrame(self._frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.content_layout = QHBoxLayout(self.content_frame)
        self.content_layout.setObjectName(u"content_layout")

        self.verticalLayout_2.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self._frame)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Home", u"Welcome Back, User!", None))
        self.latest_button.setText(QCoreApplication.translate("Home", u"Latest", None))
        self.groups_button.setText(QCoreApplication.translate("Home", u"Groups", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 600)
        self.main_frame = QWidget(MainWindow)
        self.main_frame.setObjectName(u"main_frame")
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_nav = QFrame(self.main_frame)
        self.side_nav.setObjectName(u"side_nav")
        self.side_nav.setMaximumSize(QSize(80, 16777215))
        self.side_nav.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 10;\n"
"	max-width: 70;\n"
"	height: 70;\n"
"	margin-left: 5;\n"
"	margin-top: 5;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        self.side_nav.setFrameShape(QFrame.NoFrame)
        self.side_nav.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.side_nav)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.side_nav)
        self.home_button.setObjectName(u"home_button")

        self.verticalLayout.addWidget(self.home_button)

        self.profile_button = QPushButton(self.side_nav)
        self.profile_button.setObjectName(u"profile_button")

        self.verticalLayout.addWidget(self.profile_button)

        self.exercise_button = QPushButton(self.side_nav)
        self.exercise_button.setObjectName(u"exercise_button")

        self.verticalLayout.addWidget(self.exercise_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.side_nav)

        self.pages_frame = QFrame(self.main_frame)
        self.pages_frame.setObjectName(u"pages_frame")
        self.pages_frame.setFrameShape(QFrame.NoFrame)
        self.pages_frame.setFrameShadow(QFrame.Raised)
        self.pages_layout = QVBoxLayout(self.pages_frame)
        self.pages_layout.setSpacing(0)
        self.pages_layout.setObjectName(u"pages_layout")
        self.pages_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.pages_frame)

        MainWindow.setCentralWidget(self.main_frame)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.exercise_button.setText(QCoreApplication.translate("MainWindow", u"Exercise", None))
    # retranslateUi


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
        MainWindow.resize(872, 603)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: #f8f9fa;\n"
"\n"
"}")
        self.main_frame = QWidget(MainWindow)
        self.main_frame.setObjectName(u"main_frame")
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_nav = QFrame(self.main_frame)
        self.side_nav.setObjectName(u"side_nav")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_nav.sizePolicy().hasHeightForWidth())
        self.side_nav.setSizePolicy(sizePolicy)
        self.side_nav.setMinimumSize(QSize(80, 80))
        self.side_nav.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setBold(False)
        self.side_nav.setFont(font)
        self.side_nav.setMouseTracking(False)
        self.side_nav.setStyleSheet(u"QFrame{\n"
"	background-color: #dee2e6;\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: #ced4da;\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 20;\n"
"	max-width: 70;\n"
"	min-width: 70;\n"
"	height: 70;\n"
"	margin-left: 5;\n"
"	margin-top: 5;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #adb5bd;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #dee2e6;\n"
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

        self.settings_button = QPushButton(self.side_nav)
        self.settings_button.setObjectName(u"settings_button")

        self.verticalLayout.addWidget(self.settings_button)

        self.library_button = QPushButton(self.side_nav)
        self.library_button.setObjectName(u"library_button")

        self.verticalLayout.addWidget(self.library_button)

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
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.library_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi


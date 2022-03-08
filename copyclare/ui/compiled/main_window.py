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
        self.side_nav.setFrameShape(QFrame.NoFrame)
        self.side_nav.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.side_nav)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.side_nav)
        self.home_button.setObjectName(u"home_button")
        icon = QIcon()
        icon.addFile(u"../../data/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.home_button)

        self.progress_button = QPushButton(self.side_nav)
        self.progress_button.setObjectName(u"progress_button")
        icon1 = QIcon()
        icon1.addFile(u"../../data/progress.png", QSize(), QIcon.Normal, QIcon.Off)
        self.progress_button.setIcon(icon1)
        self.progress_button.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.progress_button)

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
        self.home_button.setText("")
        self.progress_button.setText("")
    # retranslateUi


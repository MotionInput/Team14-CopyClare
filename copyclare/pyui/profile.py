# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_profile_page(object):
    def setupUi(self, profile_page):
        if not profile_page.objectName():
            profile_page.setObjectName(u"profile_page")
        profile_page.resize(757, 700)
        profile_page.setMinimumSize(QSize(0, 700))
        profile_page.setStyleSheet(u"QFrame{\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #000000;\n"
"	font-size: 30px;\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(profile_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(profile_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 700))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 745, 700))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 673, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(profile_page)

        QMetaObject.connectSlotsByName(profile_page)
    # setupUi

    def retranslateUi(self, profile_page):
        profile_page.setWindowTitle(QCoreApplication.translate("profile_page", u"Frame", None))
    # retranslateUi


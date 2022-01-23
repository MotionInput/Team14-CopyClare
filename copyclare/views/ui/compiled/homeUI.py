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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(900, 600)
        Home.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.copyclare_logo = QLabel(Home)
        self.copyclare_logo.setObjectName(u"copyclare_logo")
        self.copyclare_logo.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Futura"])
        font.setPointSize(25)
        font.setBold(True)
        font.setKerning(False)
        self.copyclare_logo.setFont(font)
        self.copyclare_logo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(151, 64, 253);")
        self.copyclare_logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.copyclare_logo)

        self.teston_label = QLabel(Home)
        self.teston_label.setObjectName(u"teston_label")

        self.verticalLayout.addWidget(self.teston_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.copyclare_logo.setText(QCoreApplication.translate("Home", u"   CopyClare", None))
        self.teston_label.setText(QCoreApplication.translate("Home", u"Testong yay", None))
    # retranslateUi


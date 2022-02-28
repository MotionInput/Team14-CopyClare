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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_main_frame(object):
    def setupUi(self, main_frame):
        if not main_frame.objectName():
            main_frame.setObjectName(u"main_frame")
        main_frame.resize(757, 574)
        main_frame.setStyleSheet(u"QFrame{\n"
"	background-color: #f8f9fa;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #000000;\n"
"	font-size: 30px;\n"
"}")
        self.verticalLayout = QVBoxLayout(main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(main_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(main_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(main_frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(main_frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(main_frame)

        QMetaObject.connectSlotsByName(main_frame)
    # setupUi

    def retranslateUi(self, main_frame):
        main_frame.setWindowTitle(QCoreApplication.translate("main_frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("main_frame", u"First Name: Adi", None))
        self.label_2.setText(QCoreApplication.translate("main_frame", u"Last Name: Bozzhanov", None))
        self.label_3.setText(QCoreApplication.translate("main_frame", u"email: adi.bozzhanov.20@ucl.ac.uk", None))
        self.label_4.setText(QCoreApplication.translate("main_frame", u"Total Exercise Time: 24 mins", None))
    # retranslateUi


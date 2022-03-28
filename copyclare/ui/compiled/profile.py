# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_main_frame(object):
    def setupUi(self, main_frame):
        if not main_frame.objectName():
            main_frame.setObjectName(u"main_frame")
        main_frame.resize(757, 574)
        main_frame.setStyleSheet(u"QFrame{\n"
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
        self.verticalLayout = QVBoxLayout(main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.retranslateUi(main_frame)

        QMetaObject.connectSlotsByName(main_frame)

    # setupUi

    def retranslateUi(self, main_frame):
        main_frame.setWindowTitle(
            QCoreApplication.translate("main_frame", u"Frame", None))

    # retranslateUi

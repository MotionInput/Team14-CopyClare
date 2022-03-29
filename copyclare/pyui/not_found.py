# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'not_found.ui'
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
    QSizePolicy, QWidget)

class Ui_not_found(object):
    def setupUi(self, not_found):
        if not not_found.objectName():
            not_found.setObjectName(u"not_found")
        not_found.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(not_found)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(not_found)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(not_found)

        QMetaObject.connectSlotsByName(not_found)
    # setupUi

    def retranslateUi(self, not_found):
        not_found.setWindowTitle(QCoreApplication.translate("not_found", u"Frame", None))
        self.label.setText(QCoreApplication.translate("not_found", u"To be Implemented...", None))
    # retranslateUi


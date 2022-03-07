# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_card.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.video_card = QFrame(Form)
        self.video_card.setObjectName(u"video_card")
        self.video_card.setMaximumSize(QSize(900, 300))
        self.verticalLayout_6 = QVBoxLayout(self.video_card)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graphicsView = QGraphicsView(self.video_card)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_6.addWidget(self.graphicsView)

        self.label_7 = QLabel(self.video_card)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_3 = QLabel(self.video_card)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.video_card)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.video_card)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"00:30", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Push ups", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"This is a good exercise", None))
    # retranslateUi


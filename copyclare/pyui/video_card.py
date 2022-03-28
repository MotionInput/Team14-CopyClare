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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 367)
        Form.setMinimumSize(QSize(300, 0))
        Form.setMaximumSize(QSize(300, 900))
        Form.setStyleSheet(u"border: 2px solid;\n"
"border-color: #929292;\n"
"color: #000000;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.video_image = QLabel(Form)
        self.video_image.setObjectName(u"video_image")
        self.video_image.setMinimumSize(QSize(0, 150))
        self.video_image.setMaximumSize(QSize(280, 160))
        self.video_image.setStyleSheet(u"border: none;")
        self.video_image.setScaledContents(True)

        self.verticalLayout.addWidget(self.video_image)

        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.title)

        self.description = QLabel(Form)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.description)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.video_image.setText("")
        self.add_btn.setText(QCoreApplication.translate("Form", u"add", None))
        self.title.setText(QCoreApplication.translate("Form", u"Title", None))
        self.description.setText(QCoreApplication.translate("Form", u"Description here.", None))
    # retranslateUi


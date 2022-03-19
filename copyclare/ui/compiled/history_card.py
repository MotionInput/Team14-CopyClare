# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_card.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(871, 228)
        Form.setStyleSheet(u"border: 2px solid;\n"
"border-bottom-color: rgb(204, 204, 204);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalFrame = QFrame(Form)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"border: none;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(self.horizontalFrame)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(0, 180))
        self.graphicsView.setMaximumSize(QSize(300, 180))
        self.graphicsView.setStyleSheet(u"border: 1px solid;\n"
"border-color: rgb(153, 153, 153);")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.verticalFrame = QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"border: none;\n"
"")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.verticalFrame)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(250, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.title)

        self.date = QLabel(self.verticalFrame)
        self.date.setObjectName(u"date")
        self.date.setMinimumSize(QSize(250, 0))
        font1 = QFont()
        font1.setPointSize(20)
        self.date.setFont(font1)
        self.date.setStyleSheet(u"border: none;\n"
"")

        self.verticalLayout.addWidget(self.date)


        self.horizontalLayout.addWidget(self.verticalFrame)


        self.horizontalLayout_2.addWidget(self.horizontalFrame)

        self.analysis_button = QPushButton(Form)
        self.analysis_button.setObjectName(u"analysis_button")
        self.analysis_button.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"../../../../../Documents/\ud83d\udcda/--UCL/-STUDY STUFF/YEAR 2/COMP0016 Systems Engineering/copyclare/prototype/pages/icon-analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analysis_button.setIcon(icon)
        self.analysis_button.setIconSize(QSize(150, 150))
        self.analysis_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.analysis_button)

        self.export_button = QPushButton(Form)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setStyleSheet(u"border: none;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../Documents/\ud83d\udcda/--UCL/-STUDY STUFF/YEAR 2/COMP0016 Systems Engineering/copyclare/prototype/pages/icon-export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_button.setIcon(icon1)
        self.export_button.setIconSize(QSize(150, 150))
        self.export_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.export_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Shoulder Exercise", None))
        self.date.setText(QCoreApplication.translate("Form", u"Date", None))
        self.analysis_button.setText("")
        self.export_button.setText("")
    # retranslateUi


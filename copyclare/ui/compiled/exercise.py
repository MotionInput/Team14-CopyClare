# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exercise.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Exercise(object):
    def setupUi(self, Exercise):
        if not Exercise.objectName():
            Exercise.setObjectName(u"Exercise")
        Exercise.resize(900, 600)
        Exercise.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        Exercise.setFrameShape(QFrame.StyledPanel)
        Exercise.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(Exercise)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Exercise)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.video_1 = QLabel(self.frame_3)
        self.video_1.setObjectName(u"video_1")
        self.video_1.setFrameShape(QFrame.NoFrame)
        self.video_1.setTextFormat(Qt.PlainText)
        self.video_1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.video_1)

        self.video_2 = QLabel(self.frame_3)
        self.video_2.setObjectName(u"video_2")
        self.video_2.setFrameShape(QFrame.NoFrame)
        self.video_2.setTextFormat(Qt.PlainText)
        self.video_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.video_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLabel {\n"
"	color: rgb(0,0,0); \n"
"	font-size: 30px;\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.angle_label = QLabel(self.frame)
        self.angle_label.setObjectName(u"angle_label")

        self.gridLayout.addWidget(self.angle_label, 0, 0, 1, 1)

        self.rep_label = QLabel(self.frame)
        self.rep_label.setObjectName(u"rep_label")

        self.gridLayout.addWidget(self.rep_label, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Exercise)

        QMetaObject.connectSlotsByName(Exercise)
    # setupUi

    def retranslateUi(self, Exercise):
        Exercise.setWindowTitle(QCoreApplication.translate("Exercise", u"Frame", None))
        self.video_1.setText("")
        self.video_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Exercise", u"Accuracy:", None))
        self.angle_label.setText(QCoreApplication.translate("Exercise", u"Angle:", None))
        self.rep_label.setText(QCoreApplication.translate("Exercise", u"Repetitions:", None))
    # retranslateUi


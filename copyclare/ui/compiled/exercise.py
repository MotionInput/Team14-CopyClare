# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exercise.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_exercise_frame(object):
    def setupUi(self, exercise_frame):
        if not exercise_frame.objectName():
            exercise_frame.setObjectName(u"exercise_frame")
        exercise_frame.resize(900, 628)
        exercise_frame.setLayoutDirection(Qt.LeftToRight)
        exercise_frame.setFrameShape(QFrame.NoFrame)
        exercise_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(exercise_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.controls_frame = QFrame(exercise_frame)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMaximumSize(QSize(300, 16777215))
        self.controls_frame.setStyleSheet(u"")
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.controls_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.video_frame = QFrame(self.controls_frame)
        self.video_frame.setObjectName(u"video_frame")
        self.video_frame.setMinimumSize(QSize(300, 300))
        self.video_frame.setMaximumSize(QSize(16777215, 300))
        self.video_frame.setFrameShape(QFrame.NoFrame)
        self.video_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.video_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.video_label = QLabel(self.video_frame)
        self.video_label.setObjectName(u"video_label")
        self.video_label.setMinimumSize(QSize(300, 300))
        self.video_label.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_3.addWidget(self.video_label)

        self.verticalLayout.addWidget(self.video_frame)

        self.graph_frame = QFrame(self.controls_frame)
        self.graph_frame.setObjectName(u"graph_frame")
        self.graph_frame.setMaximumSize(QSize(16777215, 200))
        self.graph_frame.setFrameShape(QFrame.NoFrame)
        self.graph_frame.setFrameShadow(QFrame.Plain)
        self.graph_frame.setLineWidth(0)
        self.graph_layout = QHBoxLayout(self.graph_frame)
        self.graph_layout.setSpacing(0)
        self.graph_layout.setObjectName(u"graph_layout")
        self.graph_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.graph_frame)

        self.data_frame = QFrame(self.controls_frame)
        self.data_frame.setObjectName(u"data_frame")
        self.data_frame.setFrameShape(QFrame.NoFrame)
        self.data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.data_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.data_frame)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout.addWidget(self.data_frame)

        self.end_button = QPushButton(self.controls_frame)
        self.end_button.setObjectName(u"end_button")
        font = QFont()
        font.setPointSize(15)
        self.end_button.setFont(font)
        self.end_button.setStyleSheet(u"QPushButton {\n"
                                      "	border: none;\n"
                                      "	background-color: #fc8892;\n"
                                      "	color: rgb(0,0,0);\n"
                                      "	height: 50;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: #ff5260;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "	background-color: #ff949d;\n"
                                      "}")
        self.end_button.setFlat(False)

        self.verticalLayout.addWidget(self.end_button)

        self.horizontalLayout.addWidget(self.controls_frame)

        self.camera_frame = QFrame(exercise_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.camera_frame.sizePolicy().hasHeightForWidth())
        self.camera_frame.setSizePolicy(sizePolicy)
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.camera_frame.setLineWidth(3)
        self.horizontalLayout_4 = QHBoxLayout(self.camera_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.camera_label = QLabel(self.camera_frame)
        self.camera_label.setObjectName(u"camera_label")

        self.horizontalLayout_4.addWidget(self.camera_label)

        self.horizontalLayout.addWidget(self.camera_frame)

        self.retranslateUi(exercise_frame)

        QMetaObject.connectSlotsByName(exercise_frame)

    # setupUi

    def retranslateUi(self, exercise_frame):
        exercise_frame.setWindowTitle(
            QCoreApplication.translate("exercise_frame", u"Frame", None))
        self.video_label.setText(
            QCoreApplication.translate("exercise_frame", u"TextLabel", None))
        self.label.setText(
            QCoreApplication.translate("exercise_frame", u"Reps: 5/16", None))
        self.end_button.setText(
            QCoreApplication.translate("exercise_frame", u"END EXERCISE",
                                       None))
        self.camera_label.setText(
            QCoreApplication.translate("exercise_frame", u"TextLabel", None))

    # retranslateUi

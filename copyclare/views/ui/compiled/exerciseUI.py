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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.copyclare_logo = QLabel(Exercise)
        self.copyclare_logo.setObjectName(u"copyclare_logo")
        self.copyclare_logo.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Futura"])
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setKerning(False)
        self.copyclare_logo.setFont(font)
        self.copyclare_logo.setStyleSheet(u"background-color: rgb(151, 64, 253);\n"
"color: rgb(255, 255, 255);")
        self.copyclare_logo.setMargin(5)

        self.verticalLayout.addWidget(self.copyclare_logo)

        self.top_layer = QWidget(Exercise)
        self.top_layer.setObjectName(u"top_layer")
        self.top_layer.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.top_layer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exercise_counter = QLabel(self.top_layer)
        self.exercise_counter.setObjectName(u"exercise_counter")
        font1 = QFont()
        font1.setFamilies([u"Futura"])
        font1.setPointSize(20)
        font1.setKerning(False)
        self.exercise_counter.setFont(font1)
        self.exercise_counter.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.exercise_counter)

        self.start_next_ex_button = QPushButton(self.top_layer)
        self.start_next_ex_button.setObjectName(u"start_next_ex_button")
        self.start_next_ex_button.setFont(font1)
        self.start_next_ex_button.setStyleSheet(u"background-color: rgb(173, 209, 255);")

        self.horizontalLayout.addWidget(self.start_next_ex_button)


        self.verticalLayout.addWidget(self.top_layer)

        self.video_layer = QWidget(Exercise)
        self.video_layer.setObjectName(u"video_layer")
        self.video_layer.setMinimumSize(QSize(0, 200))
        self.video_layer.setMaximumSize(QSize(16777215, 250))
        self.video_layer.setStyleSheet(u"border-color: rgb(185, 189, 189);")
        self.horizontalLayout_2 = QHBoxLayout(self.video_layer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sample_video_holder = QGraphicsView(self.video_layer)
        self.sample_video_holder.setObjectName(u"sample_video_holder")

        self.horizontalLayout_2.addWidget(self.sample_video_holder)

        self.user_video_holder = QGraphicsView(self.video_layer)
        self.user_video_holder.setObjectName(u"user_video_holder")

        self.horizontalLayout_2.addWidget(self.user_video_holder)


        self.verticalLayout.addWidget(self.video_layer)

        self.bottom_layer = QWidget(Exercise)
        self.bottom_layer.setObjectName(u"bottom_layer")
        self.bottom_layer.setMinimumSize(QSize(0, 180))
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_layer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left_column = QWidget(self.bottom_layer)
        self.left_column.setObjectName(u"left_column")
        self.verticalLayout_2 = QVBoxLayout(self.left_column)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rep_counter = QLabel(self.left_column)
        self.rep_counter.setObjectName(u"rep_counter")
        font2 = QFont()
        font2.setFamilies([u"Futura"])
        font2.setPointSize(18)
        font2.setKerning(False)
        self.rep_counter.setFont(font2)
        self.rep_counter.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.rep_counter)

        self.buttons_row = QWidget(self.left_column)
        self.buttons_row.setObjectName(u"buttons_row")
        self.horizontalLayout_4 = QHBoxLayout(self.buttons_row)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.end_session_button = QPushButton(self.buttons_row)
        self.end_session_button.setObjectName(u"end_session_button")
        self.end_session_button.setFont(font1)
        self.end_session_button.setStyleSheet(u"background-color: rgb(253, 138, 139);")

        self.horizontalLayout_4.addWidget(self.end_session_button)

        self.break_button = QPushButton(self.buttons_row)
        self.break_button.setObjectName(u"break_button")
        self.break_button.setFont(font1)
        self.break_button.setStyleSheet(u"background-color: rgb(254, 181, 133);")

        self.horizontalLayout_4.addWidget(self.break_button)


        self.verticalLayout_2.addWidget(self.buttons_row)


        self.horizontalLayout_3.addWidget(self.left_column)

        self.graph_holder = QWidget(self.bottom_layer)
        self.graph_holder.setObjectName(u"graph_holder")
        self.graph_holder.setStyleSheet(u"border-color: rgb(185, 189, 189);")
        self.verticalLayout_3 = QVBoxLayout(self.graph_holder)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_3.addWidget(self.graph_holder)


        self.verticalLayout.addWidget(self.bottom_layer)


        self.retranslateUi(Exercise)

        QMetaObject.connectSlotsByName(Exercise)
    # setupUi

    def retranslateUi(self, Exercise):
        Exercise.setWindowTitle(QCoreApplication.translate("Exercise", u"Frame", None))
        self.copyclare_logo.setText(QCoreApplication.translate("Exercise", u"   CopyClare", None))
        self.exercise_counter.setText(QCoreApplication.translate("Exercise", u"X of Y exercises left", None))
        self.start_next_ex_button.setText(QCoreApplication.translate("Exercise", u"Start Next Exercise", None))
        self.rep_counter.setText(QCoreApplication.translate("Exercise", u"X of Y times left", None))
        self.end_session_button.setText(QCoreApplication.translate("Exercise", u"End Session", None))
        self.break_button.setText(QCoreApplication.translate("Exercise", u"Take a Break", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
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

        self.top_layer = QWidget(Home)
        self.top_layer.setObjectName(u"top_layer")
        self.top_layer.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setKerning(False)
        self.top_layer.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.top_layer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.welcome_text = QLabel(self.top_layer)
        self.welcome_text.setObjectName(u"welcome_text")
        font2 = QFont()
        font2.setFamilies([u"Futura"])
        font2.setPointSize(20)
        font2.setKerning(False)
        self.welcome_text.setFont(font2)
        self.welcome_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.welcome_text)

        self.track_progress_button = QPushButton(self.top_layer)
        self.track_progress_button.setObjectName(u"track_progress_button")
        self.track_progress_button.setFont(font2)
        self.track_progress_button.setStyleSheet(u"background-color: rgb(173, 209, 255);")

        self.horizontalLayout.addWidget(self.track_progress_button)


        self.verticalLayout.addWidget(self.top_layer)

        self.main_video_box = QWidget(Home)
        self.main_video_box.setObjectName(u"main_video_box")
        self.main_video_box.setMinimumSize(QSize(0, 200))
        self.main_video_box.setFont(font2)
        self.main_video_box.setStyleSheet(u"border: 2px solid;\n"
"border-color: rgb(185, 189, 189);")
        self.horizontalLayout_2 = QHBoxLayout(self.main_video_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.video_preview_holder = QGraphicsView(self.main_video_box)
        self.video_preview_holder.setObjectName(u"video_preview_holder")
        self.video_preview_holder.setMinimumSize(QSize(200, 0))
        self.video_preview_holder.setStyleSheet(u"border-color: rgb(223, 227, 227);")

        self.horizontalLayout_2.addWidget(self.video_preview_holder)

        self.exercise_detail_box = QWidget(self.main_video_box)
        self.exercise_detail_box.setObjectName(u"exercise_detail_box")
        self.exercise_detail_box.setMinimumSize(QSize(450, 0))
        self.exercise_detail_box.setFont(font2)
        self.exercise_detail_box.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(self.exercise_detail_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.exercise_name_text = QLabel(self.exercise_detail_box)
        self.exercise_name_text.setObjectName(u"exercise_name_text")
        self.exercise_name_text.setFont(font2)

        self.verticalLayout_3.addWidget(self.exercise_name_text)

        self.tags_box = QWidget(self.exercise_detail_box)
        self.tags_box.setObjectName(u"tags_box")
        self.tags_box.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.tags_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.shoulders_tag = QLabel(self.tags_box)
        self.shoulders_tag.setObjectName(u"shoulders_tag")
        self.shoulders_tag.setMinimumSize(QSize(100, 40))
        self.shoulders_tag.setMaximumSize(QSize(100, 40))
        font3 = QFont()
        font3.setFamilies([u"Futura"])
        font3.setPointSize(15)
        font3.setKerning(False)
        self.shoulders_tag.setFont(font3)
        self.shoulders_tag.setStyleSheet(u"background-color: rgb(254, 198, 79);")
        self.shoulders_tag.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.shoulders_tag)

        self.sports_tag = QLabel(self.tags_box)
        self.sports_tag.setObjectName(u"sports_tag")
        self.sports_tag.setMinimumSize(QSize(100, 40))
        self.sports_tag.setMaximumSize(QSize(100, 40))
        self.sports_tag.setFont(font3)
        self.sports_tag.setStyleSheet(u"background-color: rgb(254, 198, 79);")
        self.sports_tag.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.sports_tag)

        self.main_video_tags_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.main_video_tags_horizontalSpacer)


        self.verticalLayout_3.addWidget(self.tags_box)

        self.duration_text = QLabel(self.exercise_detail_box)
        self.duration_text.setObjectName(u"duration_text")
        font4 = QFont()
        font4.setFamilies([u"Futura"])
        font4.setPointSize(17)
        font4.setKerning(False)
        self.duration_text.setFont(font4)

        self.verticalLayout_3.addWidget(self.duration_text)


        self.horizontalLayout_2.addWidget(self.exercise_detail_box)

        self.start_exercise_button = QPushButton(self.main_video_box)
        self.start_exercise_button.setObjectName(u"start_exercise_button")
        self.start_exercise_button.setMinimumSize(QSize(130, 60))
        self.start_exercise_button.setFont(font3)
        self.start_exercise_button.setStyleSheet(u"background-color: rgb(188, 199, 255);\n"
"border-style: outset;")

        self.horizontalLayout_2.addWidget(self.start_exercise_button, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.main_video_box, 0, Qt.AlignTop)

        self.library_box = QWidget(Home)
        self.library_box.setObjectName(u"library_box")
        self.library_box.setMinimumSize(QSize(0, 230))
        self.library_box.setStyleSheet(u"border: 2px solid;\n"
"border-color: rgb(185, 189, 189);")
        self.verticalLayout_2 = QVBoxLayout(self.library_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.library_text = QLabel(self.library_box)
        self.library_text.setObjectName(u"library_text")
        self.library_text.setFont(font2)
        self.library_text.setStyleSheet(u"border-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.library_text)

        self.library_tags_box = QWidget(self.library_box)
        self.library_tags_box.setObjectName(u"library_tags_box")
        self.library_tags_box.setMinimumSize(QSize(0, 160))
        self.library_tags_box.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(self.library_tags_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lib_shoulders_tag = QLabel(self.library_tags_box)
        self.lib_shoulders_tag.setObjectName(u"lib_shoulders_tag")
        self.lib_shoulders_tag.setMinimumSize(QSize(100, 40))
        self.lib_shoulders_tag.setMaximumSize(QSize(100, 40))
        self.lib_shoulders_tag.setFont(font3)
        self.lib_shoulders_tag.setStyleSheet(u"background-color: rgb(254, 198, 79);")
        self.lib_shoulders_tag.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lib_shoulders_tag, 0, 0, 1, 1)

        self.lib_sports_tag = QLabel(self.library_tags_box)
        self.lib_sports_tag.setObjectName(u"lib_sports_tag")
        self.lib_sports_tag.setMinimumSize(QSize(100, 40))
        self.lib_sports_tag.setMaximumSize(QSize(100, 40))
        self.lib_sports_tag.setFont(font3)
        self.lib_sports_tag.setStyleSheet(u"background-color: rgb(254, 198, 79);")
        self.lib_sports_tag.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lib_sports_tag, 0, 1, 1, 1)

        self.grid_row1_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.grid_row1_horizontalSpacer, 0, 2, 1, 1)

        self.grid_col3_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.grid_col3_verticalSpacer, 1, 2, 1, 1)

        self.grid_col1_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.grid_col1_verticalSpacer, 1, 0, 1, 1)

        self.grid_col2_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.grid_col2_verticalSpacer, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.library_tags_box)


        self.verticalLayout.addWidget(self.library_box)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.copyclare_logo.setText(QCoreApplication.translate("Home", u"   CopyClare", None))
        self.welcome_text.setText(QCoreApplication.translate("Home", u"Welcome back, UserName!", None))
        self.track_progress_button.setText(QCoreApplication.translate("Home", u"Track Progress", None))
        self.exercise_name_text.setText(QCoreApplication.translate("Home", u"[Shoulder] exercise", None))
        self.shoulders_tag.setText(QCoreApplication.translate("Home", u"[Shoulders]", None))
        self.sports_tag.setText(QCoreApplication.translate("Home", u"[Sports]", None))
        self.duration_text.setText(QCoreApplication.translate("Home", u"Duration: X hour(s) Y min(s)", None))
        self.start_exercise_button.setText(QCoreApplication.translate("Home", u"Start Day X", None))
        self.library_text.setText(QCoreApplication.translate("Home", u"Library:", None))
        self.lib_shoulders_tag.setText(QCoreApplication.translate("Home", u"[Shoulders]", None))
        self.lib_sports_tag.setText(QCoreApplication.translate("Home", u"[Sports]", None))
    # retranslateUi


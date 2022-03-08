# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis.ui'
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
    QLabel, QLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(933, 869)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
        Home.setMinimumSize(QSize(933, 717))
        Home.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(Home)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16777215, 100))
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.title_frame)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel{\n"
"	color: #000000;\n"
"\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout.addWidget(self.title_frame)

        self._frame = QFrame(Home)
        self._frame.setObjectName(u"_frame")
        self._frame.setFrameShape(QFrame.NoFrame)
        self._frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self._frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self._frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_frame = QFrame(self.content_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.text_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.name_frame = QFrame(self.text_frame)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.name_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.name_frame_title = QLabel(self.name_frame)
        self.name_frame_title.setObjectName(u"name_frame_title")

        self.verticalLayout_5.addWidget(self.name_frame_title)

        self.name = QLabel(self.name_frame)
        self.name.setObjectName(u"name")

        self.verticalLayout_5.addWidget(self.name)


        self.verticalLayout_3.addWidget(self.name_frame)

        self.description_frame = QFrame(self.text_frame)
        self.description_frame.setObjectName(u"description_frame")
        self.description_frame.setFrameShape(QFrame.StyledPanel)
        self.description_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.description_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.descriptions_frame_title = QLabel(self.description_frame)
        self.descriptions_frame_title.setObjectName(u"descriptions_frame_title")

        self.verticalLayout_8.addWidget(self.descriptions_frame_title)

        self.description = QLabel(self.description_frame)
        self.description.setObjectName(u"description")

        self.verticalLayout_8.addWidget(self.description)


        self.verticalLayout_3.addWidget(self.description_frame)

        self.date_frame = QFrame(self.text_frame)
        self.date_frame.setObjectName(u"date_frame")
        self.date_frame.setFrameShape(QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.date_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.date_frame_title = QLabel(self.date_frame)
        self.date_frame_title.setObjectName(u"date_frame_title")

        self.verticalLayout_6.addWidget(self.date_frame_title)

        self.date = QLabel(self.date_frame)
        self.date.setObjectName(u"date")

        self.verticalLayout_6.addWidget(self.date)


        self.verticalLayout_3.addWidget(self.date_frame)

        self.repetitions_frame = QFrame(self.text_frame)
        self.repetitions_frame.setObjectName(u"repetitions_frame")
        self.repetitions_frame.setFrameShape(QFrame.StyledPanel)
        self.repetitions_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.repetitions_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.repetitions_frame_title = QLabel(self.repetitions_frame)
        self.repetitions_frame_title.setObjectName(u"repetitions_frame_title")

        self.verticalLayout_7.addWidget(self.repetitions_frame_title)

        self.repetitions = QLabel(self.repetitions_frame)
        self.repetitions.setObjectName(u"repetitions")

        self.verticalLayout_7.addWidget(self.repetitions)


        self.verticalLayout_3.addWidget(self.repetitions_frame)

        self.accuracy_frame = QFrame(self.text_frame)
        self.accuracy_frame.setObjectName(u"accuracy_frame")
        self.accuracy_frame.setFrameShape(QFrame.StyledPanel)
        self.accuracy_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.accuracy_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.accuracy_frame_title = QLabel(self.accuracy_frame)
        self.accuracy_frame_title.setObjectName(u"accuracy_frame_title")

        self.verticalLayout_4.addWidget(self.accuracy_frame_title)

        self.accuracy = QLabel(self.accuracy_frame)
        self.accuracy.setObjectName(u"accuracy")

        self.verticalLayout_4.addWidget(self.accuracy)


        self.verticalLayout_3.addWidget(self.accuracy_frame)

        self.back_button = QPushButton(self.text_frame)
        self.back_button.setObjectName(u"back_button")

        self.verticalLayout_3.addWidget(self.back_button)


        self.horizontalLayout_2.addWidget(self.text_frame)

        self.graphics_frame = QFrame(self.content_frame)
        self.graphics_frame.setObjectName(u"graphics_frame")
        self.graphics_frame.setMaximumSize(QSize(500, 16777215))
        self.graphics_frame.setFrameShape(QFrame.StyledPanel)
        self.graphics_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.graphics_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.graphicsView = QGraphicsView(self.graphics_frame)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_9.addWidget(self.graphicsView)

        self.graphicsView_2 = QGraphicsView(self.graphics_frame)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_9.addWidget(self.graphicsView_2)


        self.horizontalLayout_2.addWidget(self.graphics_frame)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self._frame)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.title.setText(QCoreApplication.translate("Home", u"Analysis", None))
        self.name_frame_title.setText(QCoreApplication.translate("Home", u"Name of Exercise:", None))
        self.name.setText(QCoreApplication.translate("Home", u"Shoulder exercise", None))
        self.descriptions_frame_title.setText(QCoreApplication.translate("Home", u"Description", None))
        self.description.setText(QCoreApplication.translate("Home", u"Slowy raise your arm and else as well", None))
        self.date_frame_title.setText(QCoreApplication.translate("Home", u"Date", None))
        self.date.setText(QCoreApplication.translate("Home", u"22-02-2022 16:30", None))
        self.repetitions_frame_title.setText(QCoreApplication.translate("Home", u"# of reps", None))
        self.repetitions.setText(QCoreApplication.translate("Home", u"10", None))
        self.accuracy_frame_title.setText(QCoreApplication.translate("Home", u"Avg. Accuracy", None))
        self.accuracy.setText(QCoreApplication.translate("Home", u"74%", None))
        self.back_button.setText(QCoreApplication.translate("Home", u"Back", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QPushButton, QScrollArea, QSizePolicy,
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
        self.motivation_frame = QFrame(Home)
        self.motivation_frame.setObjectName(u"motivation_frame")
        self.motivation_frame.setMaximumSize(QSize(16777215, 100))
        self.motivation_frame.setFrameShape(QFrame.NoFrame)
        self.motivation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.motivation_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.motivation_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: #000000;\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.motivation_frame)

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
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.todays_work_frame = QFrame(self.content_frame)
        self.todays_work_frame.setObjectName(u"todays_work_frame")
        self.todays_work_frame.setFrameShape(QFrame.StyledPanel)
        self.todays_work_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.todays_work_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_frame = QFrame(self.todays_work_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title = QLabel(self.title_frame)
        self.title.setObjectName(u"title")

        self.horizontalLayout_3.addWidget(self.title)


        self.verticalLayout_3.addWidget(self.title_frame)

        self.frame = QFrame(self.todays_work_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 841, 290))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.nextButton = QPushButton(self.frame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMaximumSize(QSize(30, 900))

        self.horizontalLayout_6.addWidget(self.nextButton)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.todays_work_frame)

        self.library_frame = QFrame(self.content_frame)
        self.library_frame.setObjectName(u"library_frame")
        self.library_frame.setFrameShape(QFrame.StyledPanel)
        self.library_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.library_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.library_title_frame = QFrame(self.library_frame)
        self.library_title_frame.setObjectName(u"library_title_frame")
        self.library_title_frame.setFrameShape(QFrame.StyledPanel)
        self.library_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.library_title_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.title_2 = QLabel(self.library_title_frame)
        self.title_2.setObjectName(u"title_2")

        self.horizontalLayout_2.addWidget(self.title_2)


        self.verticalLayout_5.addWidget(self.library_title_frame)

        self.frame_2 = QFrame(self.library_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollArea_2 = QScrollArea(self.frame_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 841, 290))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_7.addWidget(self.scrollArea_2)

        self.nextButton2 = QPushButton(self.frame_2)
        self.nextButton2.setObjectName(u"nextButton2")
        self.nextButton2.setMaximumSize(QSize(30, 900))

        self.horizontalLayout_7.addWidget(self.nextButton2)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.library_frame)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self._frame)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Home", u"You can do this, <name>!", None))
        self.title.setText(QCoreApplication.translate("Home", u"Today's Exercises", None))
        self.nextButton.setText(QCoreApplication.translate("Home", u">", None))
        self.title_2.setText(QCoreApplication.translate("Home", u"Library", None))
        self.nextButton2.setText(QCoreApplication.translate("Home", u">", None))
    # retranslateUi


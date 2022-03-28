# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_addition.ui'
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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_video_addition(object):
    def setupUi(self, video_addition):
        if not video_addition.objectName():
            video_addition.setObjectName(u"video_addition")
        video_addition.resize(981, 855)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(video_addition.sizePolicy().hasHeightForWidth())
        video_addition.setSizePolicy(sizePolicy)
        video_addition.setMinimumSize(QSize(800, 600))
        video_addition.setMaximumSize(QSize(16000, 16777215))
        video_addition.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(video_addition)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(video_addition)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16000, 100))
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.title_frame)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 60))
        self.title.setMaximumSize(QSize(16000, 16777215))
        font = QFont()
        self.title.setFont(font)
        self.title.setStyleSheet(u"background-color: #35638e;\n"
"color: rgb(255, 255, 255);\n"
"padding: 15px;\n"
"font-size: 30px")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout.addWidget(self.title_frame)

        self._frame = QFrame(video_addition)
        self._frame.setObjectName(u"_frame")
        self._frame.setMaximumSize(QSize(16000, 16777215))
        self._frame.setFrameShape(QFrame.NoFrame)
        self._frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self._frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self._frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMaximumSize(QSize(16000, 16777215))
        self.content_frame.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_frame = QFrame(self.content_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setMaximumSize(QSize(16000, 16777215))
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.text_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.states = QFrame(self.text_frame)
        self.states.setObjectName(u"states")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.states.sizePolicy().hasHeightForWidth())
        self.states.setSizePolicy(sizePolicy1)
        self.states.setMaximumSize(QSize(16000, 300))
        self.states.setStyleSheet(u"QPushButton{\n"
"		border-radius: 30px;\n"
"		border-style:solid;\n"
"  		border-width:3px;\n"
"		border-color: rgb(0, 0, 0);\n"
"}")
        self.states.setFrameShape(QFrame.StyledPanel)
        self.states.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.states)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.browse_button = QPushButton(self.states)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setMaximumSize(QSize(16000, 16777215))
        self.browse_button.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.horizontalLayout_3.addWidget(self.browse_button)

        self.label = QLabel(self.states)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.upload_button = QPushButton(self.states)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setMaximumSize(QSize(16000, 16777215))
        self.upload_button.setStyleSheet(u"background-color: rgb(186, 186, 186);")

        self.horizontalLayout_3.addWidget(self.upload_button)


        self.verticalLayout_3.addWidget(self.states)

        self.input_area = QFrame(self.text_frame)
        self.input_area.setObjectName(u"input_area")
        self.input_area.setMaximumSize(QSize(16000, 16777215))
        self.input_area.setFrameShape(QFrame.StyledPanel)
        self.input_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.input_area)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.video_name_title = QLabel(self.input_area)
        self.video_name_title.setObjectName(u"video_name_title")
        self.video_name_title.setMaximumSize(QSize(16000, 16777215))
        font1 = QFont()
        font1.setBold(True)
        self.video_name_title.setFont(font1)

        self.verticalLayout_7.addWidget(self.video_name_title)

        self.video_name_editor = QTextEdit(self.input_area)
        self.video_name_editor.setObjectName(u"video_name_editor")
        sizePolicy.setHeightForWidth(self.video_name_editor.sizePolicy().hasHeightForWidth())
        self.video_name_editor.setSizePolicy(sizePolicy)
        self.video_name_editor.setMaximumSize(QSize(16777215, 600))

        self.verticalLayout_7.addWidget(self.video_name_editor)

        self.description = QLabel(self.input_area)
        self.description.setObjectName(u"description")
        self.description.setFont(font1)

        self.verticalLayout_7.addWidget(self.description)

        self.description_editor = QTextEdit(self.input_area)
        self.description_editor.setObjectName(u"description_editor")
        sizePolicy.setHeightForWidth(self.description_editor.sizePolicy().hasHeightForWidth())
        self.description_editor.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.description_editor)

        self.tags = QLabel(self.input_area)
        self.tags.setObjectName(u"tags")
        self.tags.setFont(font1)

        self.verticalLayout_7.addWidget(self.tags)

        self.tags_editor = QTextEdit(self.input_area)
        self.tags_editor.setObjectName(u"tags_editor")
        sizePolicy.setHeightForWidth(self.tags_editor.sizePolicy().hasHeightForWidth())
        self.tags_editor.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.tags_editor)

        self.confirm_button = QPushButton(self.input_area)
        self.confirm_button.setObjectName(u"confirm_button")

        self.verticalLayout_7.addWidget(self.confirm_button)


        self.verticalLayout_3.addWidget(self.input_area)

        self.back_button = QPushButton(self.text_frame)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMaximumSize(QSize(16000, 16777215))
        self.back_button.setStyleSheet(u"background-color: rgb(171, 185, 255);")

        self.verticalLayout_3.addWidget(self.back_button)


        self.horizontalLayout_2.addWidget(self.text_frame)

        self.video_trimmer = QFrame(self.content_frame)
        self.video_trimmer.setObjectName(u"video_trimmer")
        self.video_trimmer.setFrameShape(QFrame.StyledPanel)
        self.video_trimmer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.video_trimmer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalSpacer = QSpacerItem(30, 15, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer)

        self.video = QVideoWidget(self.video_trimmer)
        self.video.setObjectName(u"video")

        self.verticalLayout_4.addWidget(self.video)

        self.horizontalSpacer_2 = QSpacerItem(30, 15, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.video_trimmer)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self._frame)


        self.retranslateUi(video_addition)

        QMetaObject.connectSlotsByName(video_addition)
    # setupUi

    def retranslateUi(self, video_addition):
        video_addition.setWindowTitle(QCoreApplication.translate("video_addition", u"Frame", None))
        self.title.setText(QCoreApplication.translate("video_addition", u"ADD VIDEO", None))
        self.browse_button.setText(QCoreApplication.translate("video_addition", u"BROWSE", None))
        self.label.setText(QCoreApplication.translate("video_addition", u"It is an arrow", None))
        self.upload_button.setText(QCoreApplication.translate("video_addition", u"UPLOAD", None))
        self.video_name_title.setText(QCoreApplication.translate("video_addition", u"Input name of video:", None))
        self.video_name_editor.setHtml(QCoreApplication.translate("video_addition", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[your text here]</span></p></body></html>", None))
        self.description.setText(QCoreApplication.translate("video_addition", u"Input description:", None))
        self.description_editor.setHtml(QCoreApplication.translate("video_addition", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[Your text here]</span></p></body></html>", None))
        self.tags.setText(QCoreApplication.translate("video_addition", u"Add tags:", None))
        self.tags_editor.setHtml(QCoreApplication.translate("video_addition", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[separate with commas]</span></p></body></html>", None))
        self.confirm_button.setText(QCoreApplication.translate("video_addition", u"Confirm", None))
        self.back_button.setText(QCoreApplication.translate("video_addition", u"Back", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exercise_list_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)


class Ui__frame(object):
    def setupUi(self, _frame):
        if not _frame.objectName():
            _frame.setObjectName(u"_frame")
        _frame.resize(1191, 485)
        _frame.setStyleSheet(u"\n"
                             "QPushButton {\n"
                             "	border: none;\n"
                             "	background-color: #ced4da;\n"
                             "	color: rgb(0,0,0);\n"
                             "	border-radius: 10;\n"
                             "	max-width: 300;\n"
                             "	min-width: 300;\n"
                             "	height: 300;\n"
                             "	margin-left: 10;\n"
                             "	margin-right: 10;\n"
                             "	margin-top: 5;\n"
                             "}\n"
                             "\n"
                             "QPushButton:hover {\n"
                             "	background-color: #adb5bd;\n"
                             "}\n"
                             "\n"
                             "QPushButton:pressed {\n"
                             "	background-color: #dee2e6;\n"
                             "}")
        self.verticalLayout = QVBoxLayout(_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(_frame)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Minimum)

        self.main_layout.addItem(self.horizontalSpacer)

        self.verticalLayout.addWidget(self.main_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                          QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.retranslateUi(_frame)

        QMetaObject.connectSlotsByName(_frame)

    # setupUi

    def retranslateUi(self, _frame):
        _frame.setWindowTitle(
            QCoreApplication.translate("_frame", u"Frame", None))

    # retranslateUi

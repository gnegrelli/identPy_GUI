# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_selection.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_file_selection(object):
    def setupUi(self, file_selection):
        if file_selection.objectName():
            file_selection.setObjectName(u"file_selection")
        file_selection.resize(827, 396)
        file_selection.setMinimumSize(QSize(827, 396))
        self.gridLayout = QGridLayout(file_selection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(file_selection)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.path = QLineEdit(file_selection)
        self.path.setObjectName(u"path")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy)
        self.path.setMaximumSize(QSize(500, 16777215))
        self.path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.path)

        self.find_path = QToolButton(file_selection)
        self.find_path.setObjectName(u"find_path")

        self.horizontalLayout.addWidget(self.find_path)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.line = QFrame(file_selection)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(file_selection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.time_col = QLineEdit(file_selection)
        self.time_col.setObjectName(u"time_col")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_col.sizePolicy().hasHeightForWidth())
        self.time_col.setSizePolicy(sizePolicy1)
        self.time_col.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.time_col.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.time_col)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(file_selection)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.input_col = QLineEdit(file_selection)
        self.input_col.setObjectName(u"input_col")
        sizePolicy1.setHeightForWidth(self.input_col.sizePolicy().hasHeightForWidth())
        self.input_col.setSizePolicy(sizePolicy1)
        self.input_col.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.input_col)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(file_selection)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.output_col = QLineEdit(file_selection)
        self.output_col.setObjectName(u"output_col")
        sizePolicy1.setHeightForWidth(self.output_col.sizePolicy().hasHeightForWidth())
        self.output_col.setSizePolicy(sizePolicy1)
        self.output_col.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.output_col)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.previous = QPushButton(file_selection)
        self.previous.setObjectName(u"previous")

        self.horizontalLayout_2.addWidget(self.previous)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.next = QPushButton(file_selection)
        self.next.setObjectName(u"next")

        self.horizontalLayout_2.addWidget(self.next)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.retranslateUi(file_selection)

        QMetaObject.connectSlotsByName(file_selection)
    # setupUi

    def retranslateUi(self, file_selection):
        file_selection.setWindowTitle(QCoreApplication.translate("file_selection", u"Form", None))
        self.label.setText(QCoreApplication.translate("file_selection", u"Importa data from:", None))
        self.find_path.setText(QCoreApplication.translate("file_selection", u"...", None))
        self.label_2.setText(QCoreApplication.translate("file_selection", u"Time column:", None))
        self.time_col.setText(QCoreApplication.translate("file_selection", u"0", None))
        self.label_3.setText(QCoreApplication.translate("file_selection", u"Inputs columns:", None))
        self.label_4.setText(QCoreApplication.translate("file_selection", u"Outputs columns:", None))
        self.previous.setText(QCoreApplication.translate("file_selection", u"Previous", None))
        self.next.setText(QCoreApplication.translate("file_selection", u"Next", None))
    # retranslateUi


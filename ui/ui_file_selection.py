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

        self.horizontalLayout.addWidget(self.path)

        self.find_path = QToolButton(file_selection)
        self.find_path.setObjectName(u"find_path")

        self.horizontalLayout.addWidget(self.find_path)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 309, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(file_selection)

        QMetaObject.connectSlotsByName(file_selection)
    # setupUi

    def retranslateUi(self, file_selection):
        file_selection.setWindowTitle(QCoreApplication.translate("file_selection", u"Form", None))
        self.label.setText(QCoreApplication.translate("file_selection", u"Importa data from:", None))
        self.find_path.setText(QCoreApplication.translate("file_selection", u"...", None))
        self.previous.setText(QCoreApplication.translate("file_selection", u"Previous", None))
        self.next.setText(QCoreApplication.translate("file_selection", u"Next", None))
    # retranslateUi


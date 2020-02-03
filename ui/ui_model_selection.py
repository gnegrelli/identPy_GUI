# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'model_selection.ui'
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

class Ui_model_selection(object):
    def setupUi(self, model_selection):
        if model_selection.objectName():
            model_selection.setObjectName(u"model_selection")
        model_selection.resize(827, 396)
        model_selection.setMinimumSize(QSize(827, 396))
        self.gridLayout = QGridLayout(model_selection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(model_selection)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 25))

        self.horizontalLayout_3.addWidget(self.label)

        self.selected_model = QComboBox(model_selection)
        self.selected_model.addItem(str())
        self.selected_model.addItem(str())
        self.selected_model.addItem(str())
        self.selected_model.addItem(str())
        self.selected_model.setObjectName(u"selected_model")
        self.selected_model.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_3.addWidget(self.selected_model)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 309, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.previous = QPushButton(model_selection)
        self.previous.setObjectName(u"previous")

        self.horizontalLayout.addWidget(self.previous)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.next = QPushButton(model_selection)
        self.next.setObjectName(u"next")

        self.horizontalLayout.addWidget(self.next)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(model_selection)

        QMetaObject.connectSlotsByName(model_selection)
    # setupUi

    def retranslateUi(self, model_selection):
        model_selection.setWindowTitle(QCoreApplication.translate("model_selection", u"Form", None))
        self.label.setText(QCoreApplication.translate("model_selection", u"Select Model", None))
        self.selected_model.setItemText(0, QCoreApplication.translate("model_selection", u"Spring-Mass", None))
        self.selected_model.setItemText(1, QCoreApplication.translate("model_selection", u"Pendulum", None))
        self.selected_model.setItemText(2, QCoreApplication.translate("model_selection", u"Linearized Z-IM Load", None))
        self.selected_model.setItemText(3, QCoreApplication.translate("model_selection", u"DFIG", None))

        self.previous.setText(QCoreApplication.translate("model_selection", u"Previous", None))
        self.next.setText(QCoreApplication.translate("model_selection", u"Next", None))
    # retranslateUi


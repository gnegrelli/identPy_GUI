# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'method_selection.ui'
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

class Ui_method_selection(object):
    def setupUi(self, method_selection):
        if method_selection.objectName():
            method_selection.setObjectName(u"method_selection")
        method_selection.resize(900, 450)
        method_selection.setMinimumSize(QSize(900, 450))
        self.gridLayout = QGridLayout(method_selection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(method_selection)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(method_selection)
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)

        self.checkBox = QCheckBox(method_selection)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(method_selection)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(method_selection)
        self.comboBox_2.addItem(str())
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 301, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(method_selection)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(method_selection)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)


        self.retranslateUi(method_selection)
        self.checkBox.clicked.connect(lambda: self.comboBox_2.setEnabled(self.checkBox.isChecked()))

        QMetaObject.connectSlotsByName(method_selection)
    # setupUi

    def retranslateUi(self, method_selection):
        method_selection.setWindowTitle(QCoreApplication.translate("method_selection", u"Form", None))
        self.label.setText(QCoreApplication.translate("method_selection", u"Select 1st method", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("method_selection", u"MVMO", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("method_selection", u"PSO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("method_selection", u"Trajectory Sensitivity", None))

        self.checkBox.setText(QCoreApplication.translate("method_selection", u"2-method identification", None))
        self.label_2.setText(QCoreApplication.translate("method_selection", u"Select 2nd method", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("method_selection", u"Trajectory Sensitivity", None))

        self.pushButton_2.setText(QCoreApplication.translate("method_selection", u"Previous", None))
        self.pushButton.setText(QCoreApplication.translate("method_selection", u"Next", None))
    # retranslateUi


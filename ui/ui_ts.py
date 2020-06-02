# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ts.ui'
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

class Ui_ts_setting(object):
    def setupUi(self, ts_setting):
        if ts_setting.objectName():
            ts_setting.setObjectName(u"ts_setting")
        ts_setting.resize(827, 396)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ts_setting.sizePolicy().hasHeightForWidth())
        ts_setting.setSizePolicy(sizePolicy)
        ts_setting.setMinimumSize(QSize(827, 396))
        self.gridLayout = QGridLayout(ts_setting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.previous = QPushButton(ts_setting)
        self.previous.setObjectName(u"previous")

        self.horizontalLayout_6.addWidget(self.previous)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.next = QPushButton(ts_setting)
        self.next.setObjectName(u"next")

        self.horizontalLayout_6.addWidget(self.next)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.scrollArea = QScrollArea(ts_setting)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 807, 248))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)

        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(ts_setting)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.label)

        self.line = QFrame(ts_setting)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.max_iteration_label = QLabel(ts_setting)
        self.max_iteration_label.setObjectName(u"max_iteration_label")
        self.max_iteration_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.max_iteration_label)

        self.max_iteration = QLineEdit(ts_setting)
        self.max_iteration.setObjectName(u"max_iteration")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.max_iteration.sizePolicy().hasHeightForWidth())
        self.max_iteration.setSizePolicy(sizePolicy3)
        self.max_iteration.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.max_iteration)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tolerance_label = QLabel(ts_setting)
        self.tolerance_label.setObjectName(u"tolerance_label")
        self.tolerance_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.tolerance_label)

        self.tolerance = QLineEdit(ts_setting)
        self.tolerance.setObjectName(u"tolerance")
        sizePolicy3.setHeightForWidth(self.tolerance.sizePolicy().hasHeightForWidth())
        self.tolerance.setSizePolicy(sizePolicy3)
        self.tolerance.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.tolerance)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)


        self.retranslateUi(ts_setting)

        QMetaObject.connectSlotsByName(ts_setting)
    # setupUi

    def retranslateUi(self, ts_setting):
        ts_setting.setWindowTitle(QCoreApplication.translate("ts_setting", u"Form", None))
        self.previous.setText(QCoreApplication.translate("ts_setting", u"Previous", None))
        self.next.setText(QCoreApplication.translate("ts_setting", u"Next", None))
        self.label.setText(QCoreApplication.translate("ts_setting", u"Trajectory Sensitivity Settings", None))
        self.max_iteration_label.setText(QCoreApplication.translate("ts_setting", u"Max. Iteration", None))
        self.tolerance_label.setText(QCoreApplication.translate("ts_setting", u"Tolerance", None))
    # retranslateUi


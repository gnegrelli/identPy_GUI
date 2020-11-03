# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mvmo.ui'
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

class Ui_mvmo_setting(object):
    def setupUi(self, mvmo_setting):
        if mvmo_setting.objectName():
            mvmo_setting.setObjectName(u"mvmo_setting")
        mvmo_setting.resize(827, 396)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mvmo_setting.sizePolicy().hasHeightForWidth())
        mvmo_setting.setSizePolicy(sizePolicy)
        mvmo_setting.setMinimumSize(QSize(827, 396))
        self.gridLayout = QGridLayout(mvmo_setting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(mvmo_setting)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label)

        self.line = QFrame(mvmo_setting)
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
        self.pop_size_label = QLabel(mvmo_setting)
        self.pop_size_label.setObjectName(u"pop_size_label")
        self.pop_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.pop_size_label)

        self.pop_size = QLineEdit(mvmo_setting)
        self.pop_size.setObjectName(u"pop_size")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pop_size.sizePolicy().hasHeightForWidth())
        self.pop_size.setSizePolicy(sizePolicy2)
        self.pop_size.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.pop_size)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.offspring_label = QLabel(mvmo_setting)
        self.offspring_label.setObjectName(u"offspring_label")
        self.offspring_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.offspring_label)

        self.offspring = QLineEdit(mvmo_setting)
        self.offspring.setObjectName(u"offspring")
        sizePolicy2.setHeightForWidth(self.offspring.sizePolicy().hasHeightForWidth())
        self.offspring.setSizePolicy(sizePolicy2)
        self.offspring.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.offspring)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.max_gen_label = QLabel(mvmo_setting)
        self.max_gen_label.setObjectName(u"max_gen_label")
        self.max_gen_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.max_gen_label)

        self.max_gen = QLineEdit(mvmo_setting)
        self.max_gen.setObjectName(u"max_gen")
        sizePolicy2.setHeightForWidth(self.max_gen.sizePolicy().hasHeightForWidth())
        self.max_gen.setSizePolicy(sizePolicy2)
        self.max_gen.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.max_gen)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tolerance_label = QLabel(mvmo_setting)
        self.tolerance_label.setObjectName(u"tolerance_label")
        self.tolerance_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.tolerance_label)

        self.tolerance = QLineEdit(mvmo_setting)
        self.tolerance.setObjectName(u"tolerance")
        sizePolicy2.setHeightForWidth(self.tolerance.sizePolicy().hasHeightForWidth())
        self.tolerance.setSizePolicy(sizePolicy2)
        self.tolerance.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.tolerance)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(mvmo_setting)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 807, 182))
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

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.previous = QPushButton(mvmo_setting)
        self.previous.setObjectName(u"previous")

        self.horizontalLayout_6.addWidget(self.previous)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.next = QPushButton(mvmo_setting)
        self.next.setObjectName(u"next")

        self.horizontalLayout_6.addWidget(self.next)

        self.estimate = QPushButton(mvmo_setting)
        self.estimate.setObjectName(u"estimate")

        self.horizontalLayout_6.addWidget(self.estimate)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)


        self.retranslateUi(mvmo_setting)

        QMetaObject.connectSlotsByName(mvmo_setting)
    # setupUi

    def retranslateUi(self, mvmo_setting):
        mvmo_setting.setWindowTitle(QCoreApplication.translate("mvmo_setting", u"Form", None))
        self.label.setText(QCoreApplication.translate("mvmo_setting", u"MVMO Settings", None))
        self.pop_size_label.setText(QCoreApplication.translate("mvmo_setting", u"Population Size", None))
        self.offspring_label.setText(QCoreApplication.translate("mvmo_setting", u"Offspring", None))
        self.max_gen_label.setText(QCoreApplication.translate("mvmo_setting", u"Max. Generation", None))
        self.tolerance_label.setText(QCoreApplication.translate("mvmo_setting", u"Tolerance", None))
        self.tolerance.setText("")
        self.previous.setText(QCoreApplication.translate("mvmo_setting", u"Previous", None))
        self.next.setText(QCoreApplication.translate("mvmo_setting", u"Next", None))
        self.estimate.setText(QCoreApplication.translate("mvmo_setting", u"Estimate", None))
    # retranslateUi


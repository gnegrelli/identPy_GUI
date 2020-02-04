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
        mvmo_setting.setMinimumSize(QSize(827, 396))
        self.gridLayout = QGridLayout(mvmo_setting)
        self.gridLayout.setObjectName(u"gridLayout")
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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pop_size.sizePolicy().hasHeightForWidth())
        self.pop_size.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.offspring.sizePolicy().hasHeightForWidth())
        self.offspring.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.max_gen.sizePolicy().hasHeightForWidth())
        self.max_gen.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.tolerance.sizePolicy().hasHeightForWidth())
        self.tolerance.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.tolerance)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 260, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)


        self.retranslateUi(mvmo_setting)

        QMetaObject.connectSlotsByName(mvmo_setting)
    # setupUi

    def retranslateUi(self, mvmo_setting):
        mvmo_setting.setWindowTitle(QCoreApplication.translate("mvmo_setting", u"Form", None))
        self.pop_size_label.setText(QCoreApplication.translate("mvmo_setting", u"Population Size", None))
        self.offspring_label.setText(QCoreApplication.translate("mvmo_setting", u"Offspring", None))
        self.max_gen_label.setText(QCoreApplication.translate("mvmo_setting", u"Max. Generation", None))
        self.tolerance_label.setText(QCoreApplication.translate("mvmo_setting", u"Tolerance", None))
        self.tolerance.setText("")
        self.previous.setText(QCoreApplication.translate("mvmo_setting", u"Previous", None))
        self.next.setText(QCoreApplication.translate("mvmo_setting", u"Next", None))
    # retranslateUi


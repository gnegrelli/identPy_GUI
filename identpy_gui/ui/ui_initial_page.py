# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'initial_page.ui'
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

class Ui_initialPage(object):
    def setupUi(self, initialPage):
        if initialPage.objectName():
            initialPage.setObjectName(u"initialPage")
        initialPage.resize(827, 396)
        initialPage.setMinimumSize(QSize(827, 396))
        self.gridLayout = QGridLayout(initialPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name = QLabel(initialPage)
        self.name.setObjectName(u"name")
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(18)
        self.name.setFont(font)
        self.name.setTextFormat(Qt.AutoText)
        self.name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name)

        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.description = QLabel(initialPage)
        self.description.setObjectName(u"description")
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.description.setFont(font1)
        self.description.setAutoFillBackground(False)
        self.description.setTextFormat(Qt.AutoText)
        self.description.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description.setWordWrap(True)
        self.description.setMargin(0)
        self.description.setIndent(0)
        self.description.setOpenExternalLinks(True)
        self.description.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout.addWidget(self.description)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.next = QPushButton(initialPage)
        self.next.setObjectName(u"next")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy)
        self.next.setMinimumSize(QSize(89, 25))
        self.next.setMaximumSize(QSize(89, 25))

        self.horizontalLayout.addWidget(self.next)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(initialPage)

        QMetaObject.connectSlotsByName(initialPage)
    # setupUi

    def retranslateUi(self, initialPage):
        initialPage.setWindowTitle(QCoreApplication.translate("initialPage", u"Form", None))
        self.name.setText(QCoreApplication.translate("initialPage", u"identPy v1.0", None))
        self.description.setText(QCoreApplication.translate("initialPage", u"<html><head/><body><p>This software was developed by Gabriel Negrelli, under advisement of Prof. Elmer Cari, as part of his Masters Project in Electrical Engineering at the University of S\u00e3o Paulo - S\u00e3o Carlos.</p><p>The software was developed at LACOSEP and its main purpose is to estimate parameters of dynamic systems models using various approaches.</p><p>This software is available at <a href=https://github.com/gnegrelli/identPy_GUI><span style=\" text-decoration: underline; color:#0000ff;\">github.com/gnegrelli/identPy_GUI</span></a></p></body></html>", None))
        self.next.setText(QCoreApplication.translate("initialPage", u"Next", None))
    # retranslateUi


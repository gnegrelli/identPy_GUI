# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results_page.ui'
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

class Ui_results(object):
    def setupUi(self, results):
        if results.objectName():
            results.setObjectName(u"results")
        results.resize(827, 396)
        results.setMinimumSize(QSize(827, 396))
        self.gridLayout = QGridLayout(results)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(results)
        self.tabWidget.setObjectName(u"tabWidget")
        palette = QPalette()
        brush = QBrush(QColor(211, 215, 207, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, QString())
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 98, 20))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 98, 20))
        self.tabWidget.addTab(self.tab_2, QString())

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(results)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(results)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.previous = QPushButton(results)
        self.previous.setObjectName(u"previous")

        self.horizontalLayout.addWidget(self.previous)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.next = QPushButton(results)
        self.next.setObjectName(u"next")

        self.horizontalLayout.addWidget(self.next)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(results)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(results)
    # setupUi

    def retranslateUi(self, results):
        results.setWindowTitle(QCoreApplication.translate("results", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("results", u"Tab 1", None))
        self.label_3.setText(QCoreApplication.translate("results", u"p1: 2", None))
        self.label_4.setText(QCoreApplication.translate("results", u"p2: -5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("results", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("results", u"Iteration #999", None))
        self.label_2.setText(QCoreApplication.translate("results", u"Error: 2.81", None))
        self.previous.setText(QCoreApplication.translate("results", u"Previous", None))
        self.next.setText(QCoreApplication.translate("results", u"Next", None))
    # retranslateUi


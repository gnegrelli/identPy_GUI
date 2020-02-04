# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_explorer.ui'
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

class Ui_file_explorer(object):
    def setupUi(self, file_explorer):
        if file_explorer.objectName():
            file_explorer.setObjectName(u"file_explorer")
        file_explorer.resize(500, 350)
        file_explorer.setMinimumSize(QSize(500, 350))
        file_explorer.setMaximumSize(QSize(800, 500))
        self.file_exp = QWidget(file_explorer)
        self.file_exp.setObjectName(u"file_exp")
        self.gridLayout = QGridLayout(self.file_exp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeView = QTreeView(self.file_exp)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEnabled(True)

        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.cancel = QPushButton(self.file_exp)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.view = QPushButton(self.file_exp)
        self.view.setObjectName(u"view")

        self.horizontalLayout.addWidget(self.view)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.open = QPushButton(self.file_exp)
        self.open.setObjectName(u"open")

        self.horizontalLayout.addWidget(self.open)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        file_explorer.setCentralWidget(self.file_exp)

        self.retranslateUi(file_explorer)

        QMetaObject.connectSlotsByName(file_explorer)
    # setupUi

    def retranslateUi(self, file_explorer):
        file_explorer.setWindowTitle(QCoreApplication.translate("file_explorer", u"MainWindow", None))
        self.cancel.setText(QCoreApplication.translate("file_explorer", u"Cancel", None))
        self.view.setText(QCoreApplication.translate("file_explorer", u"View", None))
        self.open.setText(QCoreApplication.translate("file_explorer", u"Open", None))
    # retranslateUi


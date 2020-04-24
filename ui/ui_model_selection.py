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
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(model_selection)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(122, 25))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.selected_model = QComboBox(model_selection)
        self.selected_model.addItem(str())
        self.selected_model.addItem(str())
        self.selected_model.addItem(str())
        self.selected_model.addItem(str())
        self.selected_model.addItem(str())
        self.selected_model.setObjectName(u"selected_model")
        self.selected_model.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_7.addWidget(self.selected_model)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(model_selection)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.path = QLineEdit(model_selection)
        self.path.setObjectName(u"path")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy)
        self.path.setMaximumSize(QSize(250, 16777215))
        self.path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.path)

        self.find_path = QToolButton(model_selection)
        self.find_path.setObjectName(u"find_path")

        self.horizontalLayout.addWidget(self.find_path)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.line = QFrame(model_selection)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.previous = QPushButton(model_selection)
        self.previous.setObjectName(u"previous")

        self.horizontalLayout_2.addWidget(self.previous)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.next = QPushButton(model_selection)
        self.next.setObjectName(u"next")

        self.horizontalLayout_2.addWidget(self.next)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.scrollArea = QScrollArea(model_selection)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 793, 547))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(40, 16777215))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.time_col = QLineEdit(self.scrollAreaWidgetContents)
        self.time_col.setObjectName(u"time_col")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.time_col.sizePolicy().hasHeightForWidth())
        self.time_col.setSizePolicy(sizePolicy2)
        self.time_col.setMaximumSize(QSize(40, 16777215))
        self.time_col.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.time_col.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.time_col)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.input_col = QLineEdit(self.scrollAreaWidgetContents)
        self.input_col.setObjectName(u"input_col")
        sizePolicy2.setHeightForWidth(self.input_col.sizePolicy().hasHeightForWidth())
        self.input_col.setSizePolicy(sizePolicy2)
        self.input_col.setMaximumSize(QSize(40, 16777215))
        self.input_col.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.input_col)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(40, 16777215))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.output_col = QLineEdit(self.scrollAreaWidgetContents)
        self.output_col.setObjectName(u"output_col")
        sizePolicy2.setHeightForWidth(self.output_col.sizePolicy().hasHeightForWidth())
        self.output_col.setSizePolicy(sizePolicy2)
        self.output_col.setMaximumSize(QSize(40, 16777215))
        self.output_col.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.output_col)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(500, 0))
        self.label_6.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 1)


        self.retranslateUi(model_selection)

        QMetaObject.connectSlotsByName(model_selection)
    # setupUi

    def retranslateUi(self, model_selection):
        model_selection.setWindowTitle(QCoreApplication.translate("model_selection", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("model_selection", u"Select model:", None))
        self.selected_model.setItemText(0, "")
        self.selected_model.setItemText(1, QCoreApplication.translate("model_selection", u"Spring-Mass", None))
        self.selected_model.setItemText(2, QCoreApplication.translate("model_selection", u"Pendulum", None))
        self.selected_model.setItemText(3, QCoreApplication.translate("model_selection", u"Linearized Z-IM Load", None))
        self.selected_model.setItemText(4, QCoreApplication.translate("model_selection", u"DFIG", None))

        self.label.setText(QCoreApplication.translate("model_selection", u"Import data from:", None))
        self.find_path.setText(QCoreApplication.translate("model_selection", u"...", None))
        self.previous.setText(QCoreApplication.translate("model_selection", u"Previous", None))
        self.next.setText(QCoreApplication.translate("model_selection", u"Next", None))
        self.label_8.setText(QCoreApplication.translate("model_selection", u"<html><head/><body><p><span style=\" font-size:8pt; color:#555753;\">Time column</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("model_selection", u"t:", None))
        self.time_col.setText(QCoreApplication.translate("model_selection", u"0", None))
        self.label_9.setText(QCoreApplication.translate("model_selection", u"<html><head/><body><p><span style=\" font-size:8pt; color:#555753;\">Input columns</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("model_selection", u"u1:", None))
        self.label_4.setText(QCoreApplication.translate("model_selection", u"u2:", None))
        self.label_6.setText(QCoreApplication.translate("model_selection", u"<html><head/><body><p align=\"justify\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia, diam eget malesuada hendrerit, arcu sem semper sapien, a egestas massa nisl pharetra massa. Phasellus ut ligula nec elit feugiat porttitor in quis odio. Phasellus quis risus augue. Integer nec lorem ullamcorper, blandit ante sit amet, dignissim lorem. Pellentesque sed molestie ligula. Nulla a tellus facilisis, mollis odio sed, viverra magna. Aenean egestas augue nisi, sit amet aliquet neque condimentum id. Praesent sit amet est dignissim, blandit nibh eu, auctor nulla. Pellentesque tempus ex eget purus tempor, eu ultrices quam lobortis. Suspendisse tristique sem ac pellentesque hendrerit. Nulla facilisi. Cras volutpat ante quis diam finibus, ut gravida orci laoreet. Mauris imperdiet, elit et finibus varius, dolor nisi venenatis tortor, sit amet porta metus diam eu sapien. </p><p align=\"justify\">Pellentesque hendrerit sollicitudin nisi at blandit. Nulla viverra commodo nisl. Pellentesque sed sem m"
                        "etus. Quisque placerat, urna sit amet volutpat viverra, ex ex ullamcorper nibh, id tempor dolor nisi vel neque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut facilisis felis et nibh tincidunt facilisis. Curabitur ultricies velit odio. Donec vel imperdiet tellus, ut blandit ligula. Vestibulum augue quam, euismod sed dolor nec, molestie consequat massa. Etiam tristique consequat ex, vitae fringilla sapien condimentum non. In non laoreet diam. Nullam tempor finibus augue, nec sagittis mauris dapibus a. Morbi in quam diam. Sed quis ex ante. Aenean vitae lacus nibh. </p><p align=\"justify\">Nulla id justo quis dui varius tempus. Phasellus in ligula urna. Maecenas semper commodo nibh id auctor. Aliquam erat volutpat. Nulla tincidunt ligula felis, sit amet dignissim mi aliquet at. Curabitur id consectetur libero. Sed eu massa non enim bibendum ultricies sed a libero. </p><p align=\"justify\">Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus m"
                        "us. Quisque in bibendum mauris. In lacinia at purus et rhoncus. Aenean at tristique diam. Maecenas accumsan elit sit amet mattis egestas. Fusce a risus leo. Nam non elit sit amet justo ultricies eleifend at nec nisi. Vivamus vehicula mi eget tempor posuere. Vestibulum mollis fermentum eros. Praesent arcu enim, sollicitudin sit amet lobortis et, mollis vitae nisi. </p></body></html>", None))
    # retranslateUi


from objects.widget import MyQWidget
from ui.ui_mvmo import Ui_mvmo_setting

from PySide2.QtWidgets import *
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)


class mvmo(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_mvmo_setting()

        super().__init__(parent)

        # Mock
        p = ['R', 'X', 'f', 'z', "X'", 'aqui']
        self.populate(p)

    def next(self):
        print(self.ui.max_gen.text())
        super().next()

    def populate(self, n):
        print('Populating screen with %d instances' % len(n))
        for i in n:
            self.add_param_row(i)

    def add_param_row(self, name):
        horizontal_layout = QHBoxLayout()

        param_name = QLabel('{} :'.format(name))
        param_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        param_name.setFixedSize(QSize(30, 25))
        horizontal_layout.addWidget(param_name)

        from_label = QLabel('from')
        from_label.setAlignment(Qt.AlignCenter)
        from_label.setFixedSize(QSize(34, 25))
        horizontal_layout.addWidget(from_label)

        lower_bound = QLineEdit()
        lower_bound.setMaximumSize(QSize(75, 75))
        horizontal_layout.addWidget(lower_bound)

        to_label = QLabel('to')
        to_label.setAlignment(Qt.AlignCenter)
        to_label.setFixedSize(QSize(15, 25))
        horizontal_layout.addWidget(to_label)

        upper_bound = QLineEdit()
        upper_bound.setMaximumSize(QSize(75, 75))
        horizontal_layout.addWidget(upper_bound)

        self.ui.verticalLayout_2.addLayout(horizontal_layout)
        # self.ui.verticalLayout_2.re

        return lower_bound, upper_bound

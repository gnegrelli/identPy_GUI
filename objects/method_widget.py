from objects import BaseWidget

from PySide2.QtWidgets import *
from PySide2.QtCore import QSize, Qt


class MethodWidget(BaseWidget, QWidget):

    def __init__(self, parent):

        super().__init__(parent)

    def populate(self, n):
        print('Populating screen with %d instances' % len(n))
        for i in n:
            l, u = self.add_param_row(i)
            self.lower_bound.append(l)
            self.upper_bound.append(u)

    def add_param_row(self, name):
        horizontal_layout = QHBoxLayout()

        param_name = QLabel('{} :'.format(name))
        param_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        param_name.setFixedSize(QSize(35, 25))
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

        return lower_bound, upper_bound

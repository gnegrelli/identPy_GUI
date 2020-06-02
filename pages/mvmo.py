import numpy as np

from objects import MethodWidget

from ui import UI_MVMO

from identpy.Method import MVMO

from PySide2.QtWidgets import QHBoxLayout, QLineEdit, QLabel
from PySide2.QtCore import QSize, Qt


class mvmo(MethodWidget):

    def __init__(self, parent):

        self.ui = UI_MVMO()

        super().__init__(parent)

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

    def next(self):
        bounds = list(zip(*self.entries))
        lower_bound = np.array([self._validate_float(lb.text()) for lb in bounds[0]])
        upper_bound = np.array([self._validate_float(ub.text()) for ub in bounds[1]])
        go_on = False if '' in list(lower_bound) + list(upper_bound) else True

        if go_on:
            self.parent.estimator.add_method(MVMO(lower_bound, upper_bound))
            print(self.parent.estimator.method1, self.parent.estimator.method2)
            super().next()

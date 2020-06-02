import numpy as np

from objects import MethodWidget

from ui import UI_TS

from identpy.Method import TS

from PySide2.QtWidgets import QHBoxLayout, QLineEdit, QLabel
from PySide2.QtCore import QSize, Qt


class ts_page(MethodWidget):

    def __init__(self, parent):

        self.ui = UI_TS()

        super().__init__(parent)

    def add_param_row(self, name):
        horizontal_layout = QHBoxLayout()

        param_name = QLabel('{} :'.format(name))
        param_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        param_name.setFixedSize(QSize(35, 25))
        horizontal_layout.addWidget(param_name)

        initial_value = QLineEdit()
        initial_value.setMaximumSize(QSize(75, 75))
        horizontal_layout.addWidget(initial_value)

        self.ui.verticalLayout_2.addLayout(horizontal_layout)

        return initial_value

    def next(self):
        p0 = np.array([self._validate_float(p.text()) for p in self.entries])
        go_on = False if '' in list(p0) else True

        if go_on:
            max_iteration = self._validate_int(self.ui.max_iteration.text(), validate=lambda x: x > 0)
            go_on = False if max_iteration == '' else True

        if go_on:
            tolerance = self._validate_float(self.ui.tolerance.text(), validate=lambda x: x > 0)
            go_on = False if tolerance == '' else True

        if go_on:
            self.parent.estimator.add_method(TS(p0, max_it=max_iteration, tol=tolerance))

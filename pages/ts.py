from objects import MethodWidget

from ui import UI_TS

from identpy.Method import TS

from PySide2.QtWidgets import *
from PySide2.QtCore import QSize, Qt


class ts_page(MethodWidget):



    def __init__(self, parent):

        self.ui = UI_TS()

        self.initial_values = []

        super().__init__(parent)

        self.populate(self.parent.estimator.model.parameters.keys())

    def populate(self, n):
        print('Populating screen with %d instances' % len(n))
        for i in n:
            p0 = self.add_param_row(i)
            self.initial_values.append(p0)

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
        p0 = [p0.text() for p0 in self.initial_values]
        print(p0)

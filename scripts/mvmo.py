from objects.widget import MyQWidget
from ui.ui_mvmo import Ui_mvmo_setting

from identpy.Method import MVMO

from PySide2.QtWidgets import *
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)


class mvmo(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_mvmo_setting()

        super().__init__(parent)

        self.lower_bound = []
        self.upper_bound = []

        self.populate(self.parent.estimator.model.parameters.keys())

    def next(self):
        print(self.ui.max_gen.text())
        lower_bound = [lb.text() for lb in self.lower_bound]
        upper_bound = [ub.text() for ub in self.upper_bound]
        print(lower_bound)
        print(upper_bound)
        if self.parent.method1 is None:
            self.parent.method1 = MVMO
        else:
            self.parent.method2 = MVMO
        print(self.parent.method1, self.parent.method2)
        super().next()

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

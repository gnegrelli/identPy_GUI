from objects import BaseWidget

from PySide2.QtWidgets import QWidget, QHBoxLayout


class MethodWidget(BaseWidget, QWidget):

    def __init__(self, parent):

        super().__init__(parent)
        self.entries = []

    def populate(self, n):
        print('Populating screen with %d instances' % len(n))
        for i in n:
            self.entries.append(self.add_param_row(i))

    def add_param_row(self, name):
        horizontal_layout = QHBoxLayout()
        self.ui.verticalLayout_2.addLayout(horizontal_layout)

        return None

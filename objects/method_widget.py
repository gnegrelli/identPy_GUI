from objects import BaseWidget

from PySide2.QtWidgets import QWidget, QHBoxLayout


class MethodWidget(BaseWidget, QWidget):

    def __init__(self, parent):

        super().__init__(parent)
        self.entries = []
        self.populate(self.parent.estimator.model.parameters.keys())

        try:
            self.ui.estimate.clicked.connect(lambda: self.estimate())
        except AttributeError:
            pass

    def populate(self, n):
        for i in n:
            self.entries.append(self.add_param_row(i))

    def add_param_row(self, name):
        horizontal_layout = QHBoxLayout()
        self.ui.verticalLayout_2.addLayout(horizontal_layout)

        return None

    def verify_settings(self):
        return True

    def next(self):
        if self.verify_settings():
            super().next()

    def estimate(self):
        if self.verify_settings():
            super().next()
            # TODO: Ideally, estimation should start when results page becomes the current page on the StackedWidget
            self.parent.estimator()

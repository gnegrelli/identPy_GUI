import sys

from PySide2.QtWidgets import *

from pages.initial_page import initial_page
from pages.model_selection import model_selection
from pages.method_selection import method_selection
from pages.results import results

from identpy.Objects import Estimator


class StackedExample(QStackedWidget):

    estimator = Estimator()
    method1 = None
    method2 = None
    model = None

    def __init__(self):
        super(StackedExample, self).__init__()

        self.setGeometry(230, 180, 900, 450)
        self.setWindowTitle('identPy v1.0')

        self.initial_page = initial_page(self)
        self.addWidget(self.initial_page)

        self.model_selection = model_selection(self)
        self.addWidget(self.model_selection)

        self.method_selection = method_selection(self)
        self.addWidget(self.method_selection)

        self.results = results(self)
        self.addWidget(self.results)

        self.currentChanged.connect(lambda _: self.currentWidget().on_focus())

        self.setCurrentIndex(0)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = StackedExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

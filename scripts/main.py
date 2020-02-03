from PySide2.QtWidgets import *
import sys

from scripts.initial_page import initial_page
from scripts.model_selection import model_selection


class StackedExample(QStackedWidget):

    def __init__(self):
        super(StackedExample, self).__init__()

        self.setGeometry(230, 180, 900, 450)
        self.setWindowTitle('identPy v1.0')

        self.initial_page = initial_page(self)
        self.addWidget(self.initial_page)

        self.model_selection = model_selection(self)
        self.addWidget(self.model_selection)

        self.setCurrentIndex(0)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = StackedExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

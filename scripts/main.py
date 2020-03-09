from PySide2.QtWidgets import *
import sys

from scripts.initial_page import initial_page
from scripts.model_selection import model_selection
from scripts.method_selection import method_selection
from scripts.file_selection import file_selection


class StackedExample(QStackedWidget):

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

        self.file_selection = file_selection(self)
        self.addWidget(self.file_selection)

        self.setCurrentIndex(0)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = StackedExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

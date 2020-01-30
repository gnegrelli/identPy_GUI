from PySide2.QtWidgets import *
import sys

from scripts.initial_page import Ui_initialPage
from scripts.second_page import Ui_secondPage


class StackedExample(QStackedWidget):

    def __init__(self):
        super(StackedExample, self).__init__()

        self.setGeometry(230, 180, 900, 450)
        self.setWindowTitle('identPy v1.0')

        self.initial_page = MyQWidget(self)
        self.second_page = MyQWidget(self)

        ui_intial_page = Ui_initialPage()
        ui_intial_page.setupUi(self.initial_page)

        ui_second_page = Ui_secondPage()
        ui_second_page.setupUi(self.second_page)

        self.addWidget(self.initial_page)
        self.addWidget(self.second_page)

        self.setCurrentIndex(0)

        self.show()


class MyQWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


def main():
    app = QApplication(sys.argv)
    ex = StackedExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

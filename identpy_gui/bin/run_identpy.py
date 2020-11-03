import sys

from PySide2.QtWidgets import QApplication

from identpy_gui.objects import MyStackedWidget


def run_identpy():
    app = QApplication(sys.argv)
    ex = MyStackedWidget()
    sys.exit(app.exec_())

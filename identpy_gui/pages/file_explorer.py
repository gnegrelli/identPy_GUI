import os
import webbrowser

from PySide2 import QtWidgets
from PySide2 import QtCore

from identpy_gui.ui import FileExplorer
from identpy_gui.objects import BaseWidget


class MyFileExplorer(FileExplorer, QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        assert isinstance(parent, BaseWidget) or parent is None, 'Parent must be MyQWidget'

        self.parent = parent
        if self.parent:
            self.parent.parent.hide()

        super(MyFileExplorer, self).__init__()
        self.setupUi(self)

        self.model = QtWidgets.QFileSystemModel()

        self.populate()

        self.open.clicked.connect(self.open_path)
        self.cancel.clicked.connect(self.cancel_file_explore)
        self.view.clicked.connect(self.view_file)

        self.show()

    def populate(self):
        path = r'\home' if os.name == 'posix' else 'C:'
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

    def open_path(self):
        self.cancel_file_explore()
        if self.parent:
            self.parent.ui.path.setText(self.model.filePath(self.treeView.currentIndex()))
        else:
            print(self.model.filePath(self.treeView.currentIndex()))

    def view_file(self):
        file_path = self.model.filePath(self.treeView.currentIndex())
        webbrowser.open(file_path)

    def cancel_file_explore(self):
        if self.parent:
            self.parent.parent.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    fb = MyFileExplorer()
    app.exec_()

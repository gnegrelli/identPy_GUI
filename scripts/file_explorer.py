from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

from ui.ui_file_explorer import Ui_file_explorer

import webbrowser


class MyFileExplorer(Ui_file_explorer, QtWidgets.QMainWindow):
    def __init__(self, text_path=None):
        assert isinstance(text_path, QtWidgets.QLineEdit) or text_path is None, 'Path must be displayed on a QLineEdit'

        super(MyFileExplorer, self).__init__()
        self.setupUi(self)

        self.model = QtWidgets.QFileSystemModel()

        self.text_path = text_path

        self.populate()

        self.open.clicked.connect(self.open_path)
        self.cancel.clicked.connect(self.cancel_file_explore)
        self.view.clicked.connect(self.view_file)

        self.show()

    def populate(self):
        path = "/home"
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

    def open_path(self):
        self.close()
        if self.text_path:
            self.text_path.setText(self.model.filePath(self.treeView.currentIndex()))
        else:
            print(self.model.filePath(self.treeView.currentIndex()))

    def view_file(self):
        file_path = self.model.filePath(self.treeView.currentIndex())
        webbrowser.open(file_path)

    def cancel_file_explore(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    fb = MyFileExplorer()
    app.exec_()

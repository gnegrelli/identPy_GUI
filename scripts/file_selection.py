from objects.widget import MyQWidget
from ui.ui_file_selection import Ui_file_selection
from PySide2 import QtWidgets
from ui.ui_file_explorer import Ui_file_explorer
from scripts.file_explorer import MyFileExplorer


def validate_filepath(path):
    valid_extensions = ['csv', 'txt', 'dat']
    if not path:
        return False
    if path.split('.')[-1] in valid_extensions:
        return True
    else:
        return False


class file_selection(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_file_selection()

        super().__init__(parent)

        self.ui.find_path.clicked.connect(lambda: self.get_filepath())

    def get_filepath(self):
        # Use Pyside2 File Dialog - filepath come out weird
        # dialog = QtWidgets.QFileDialog()
        # self.parent.hide()
        # name = dialog.getOpenFileName(self, "Open File", "/home", "Text Files (*.csv *.txt *.dat)")
        # self.parent.show()
        # self.ui.path.setText(name[0])

        # Use MyFileExplorer
        self.file_browser = MyFileExplorer(self)

    def next(self):
        print('path:', self.ui.path.text())
        print(validate_filepath(self.ui.path.text()))
        print(self.ui.time_col.text())
        print(self.ui.input_col.text())
        print(self.ui.output_col.text())
        super().next()


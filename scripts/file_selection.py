from objects.widget import MyQWidget
from ui.ui_file_selection import Ui_file_selection
from PySide2 import QtWidgets
from ui.ui_file_explorer import Ui_file_explorer
from scripts.file_explorer import MyFileExplorer


class file_selection(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_file_selection()

        super().__init__(parent)

        self.ui.find_path.clicked.connect(lambda: self.get_filepath())

    def get_filepath(self):
        # Use Pyside2 File Dialog - file name is weird
        # dialog = QtWidgets.QFileDialog()
        # self.parent.hide()
        # name = dialog.getOpenFileName(self, "Open File", "/home", "Text Files (*.csv *.txt *.dat)")
        # self.parent.show()
        # self.ui.path.setText(name[0])

        # Use MyFileExplorer
        self.file_browser = MyFileExplorer(self.ui.path)

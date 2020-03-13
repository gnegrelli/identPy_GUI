from objects.widget import MyQWidget
from ui.ui_file_selection import Ui_file_selection

from scripts.file_explorer import MyFileExplorer


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
        path = self.validate_entry(entry=self.ui.path.text(), type_=['file'],
                                   valid=lambda x: x.split('.')[-1] in ['csv', 'txt', 'dat'])
        print("return path: <type {}> '{}'".format(type(path), path))

        time_col = self.validate_entry(entry=self.ui.time_col.text(), type_=['int'], valid=lambda x: x == 0)
        print("return time col: <type {}> '{}'".format(type(time_col), time_col))

        input_col = self.validate_entry(entry=self.ui.input_col.text(), type_=['float'])
        print("return input col: <type {}> '{}'".format(type(input_col), input_col))

        output_col = self.validate_entry(entry=self.ui.output_col.text(), type_=['range'])
        print("return output col: <type {}> '{}'".format(type(output_col), output_col))

        super().next()

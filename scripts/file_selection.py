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
        print('path:', self.ui.path.text())
        # path = self.validate_filepath(self.ui.path.text())
        # print('return path:', path)
        print('time', self.ui.time_col.text())
        # time_col = self.validate_cols(self.ui.time_col.text(), 'time')
        # print(time_col)
        print('input', self.ui.input_col.text())
        input_col = self.validate_cols(self.ui.input_col.text(), 'input')
        print(input_col)
        print('output', self.ui.output_col.text())
        output_col = self.validate_cols(self.ui.output_col.text(), 'output')
        print(output_col)
        super().next()

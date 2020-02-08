from objects.widget import MyQWidget
from ui.ui_file_selection import Ui_file_selection

from scripts.file_explorer import MyFileExplorer

from PySide2 import QtWidgets

import re


def warning_message(msg_title='', msg_text=''):
    msgbox = QtWidgets.QMessageBox()
    msgbox.setText(msg_title)
    msgbox.setInformativeText(msg_text)
    msgbox.setIcon(QtWidgets.QMessageBox.Warning)
    msgbox.exec_()


def validate_filepath(path='', valid_extensions=['csv', 'txt', 'dat']):
    if path and path.split('.')[-1] in valid_extensions:
        return path
    else:
        warning_message('Invalide File', 'Only .txt, .csv, and .dat files are supported.')
        return ''


def validate_cols(cols='', col_name=''):
    # Match any char that is not a digit, whitespace, comma or hyphen
    pattern = re.compile(r'[!\d\s,-]')
    if re.match(pattern, cols) or not cols:
        warning_message('Invalid Index: ' + col_name.title(),
                        'Column indices must be integer, list of integers or range.')
        return ''

    if '-' in cols:
        col_range = cols.split('-')
        if len(col_range) != 2 or not col_range[-1]:
            warning_message('Invalid Index: ' + col_name.title(),
                            'Column indices must be integer, list of integers or range.')
            return ''
        start = eval(col_range[0])
        stop = eval(col_range[1])
        if not isinstance(start, int) or not isinstance(stop, int):
            warning_message('Invalid Index: ' + col_name.title(),
                            'Column indices must be integer, list of integers or range.')
            return ''
        cols = list(range(start, stop + 1))
        if 0 in cols:
            warning_message('Invalid Index: ' + col_name.title(),
                            'Index 0 is reserved for time data.')
        return cols

    return ''


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
        # path = validate_filepath(self.ui.path.text())
        # print('return path:', path)
        print('time', self.ui.time_col.text())
        # time_col = validate_cols(self.ui.time_col.text(), 'time')
        # print(time_col)
        print('input', self.ui.input_col.text())
        input_col = validate_cols(self.ui.input_col.text(), 'input')
        print(input_col)
        print('output', self.ui.output_col.text())
        output_col = validate_cols(self.ui.output_col.text(), 'output')
        print(output_col)
        super().next()

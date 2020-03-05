from PySide2.QtWidgets import QWidget, QMessageBox
import re


class MyQWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        assert hasattr(self, 'ui'), "Page must have UI"

        self.ui.setupUi(self)

        try:
            self.ui.next.clicked.connect(lambda: self.next())
        except AttributeError:
            pass

        try:
            self.ui.previous.clicked.connect(lambda: self.previous())
        except AttributeError:
            pass

    def next(self):
        self.parent.setCurrentIndex(self.parent.currentIndex() + 1)

    def previous(self):
        self.parent.setCurrentIndex(self.parent.currentIndex() - 1)

    @staticmethod
    def warning_message(msg_title='', msg_text=''):
        msgbox = QMessageBox()
        msgbox.setText(msg_title)
        msgbox.setInformativeText(msg_text)
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.exec_()

    def validate_filepath(self, path='', valid_extensions=['csv', 'txt', 'dat']):
        if path and path.split('.')[-1] in valid_extensions:
            return path
        else:
            self.warning_message('Invalide File', 'Only .txt, .csv, and .dat files are supported.')
            return ''

    def validate_cols(self, cols='', col_name=''):
        # Match any char that is not a digit, whitespace, comma or hyphen
        pattern = re.compile(r'[!\d\s,-]')
        if re.match(pattern, cols) or not cols:
            self.warning_message('Invalid Index: ' + col_name.title(),
                                 'Column indices must be integer, list of integers or range.')
            return ''

        if '-' in cols:
            col_range = cols.split('-')
            if len(col_range) != 2 or not col_range[-1]:
                self.warning_message('Invalid Index: ' + col_name.title(),
                                     'Column indices must be integer, list of integers or range.')
                return ''
            start = eval(col_range[0])
            stop = eval(col_range[1])
            if not isinstance(start, int) or not isinstance(stop, int):
                self.warning_message('Invalid Index: ' + col_name.title(),
                                     'Column indices must be integer, list of integers or range.')
                return ''
            cols = list(range(start, stop + 1))
            if 0 in cols:
                self.warning_message('Invalid Index: ' + col_name.title(),
                                     'Index 0 is reserved for time data.')
            return cols

        return ''

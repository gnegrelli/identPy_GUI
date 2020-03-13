import re
import os

from PySide2.QtWidgets import QWidget, QMessageBox


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

    # TODO: Pass a function in `valid` using lambda
    def validate_entry(self, entry=None, valid=lambda x: True, type_=None):
        assert isinstance(entry, str), 'Entry must be a string'
        assert isinstance(type_, list), 'Possible types must be given in a list'

        func = {
            'file': lambda x, y: self._validate_filepath(x, y),
            'range': lambda x, y: print('Not implemented yet!'),
            'int': lambda x, y: self._validate_int(x, y),
            'float': lambda x, y: self._validate_float(x, y),
            'str': lambda x, y: print('Not implemented yet!'),
        }
        for typ in type_:
            ret = func[typ](entry, valid)
        return ret

    # Internal method to validate filepaths
    def _validate_filepath(self, path='', validate=lambda x: True):
        assert isinstance(path, str), 'Path given is not a string'
        assert callable(validate), 'File extensions validation must be a function'

        # Check if path exists
        if not os.path.exists(path):
            self.warning_message('Invalide File', 'Path does not exists.')
            return ''

        # Check if file has valid extension
        if validate(path):
            return path
        else:
            self.warning_message('Invalide File', 'Only .txt, .csv, and .dat files are supported.')
            return ''

    # Internal method to validate int numbers
    def _validate_int(self, value, validate=lambda x: True):
        assert isinstance(value, str), 'Value must be a string'
        assert callable(validate), 'File extensions validation must be a function'

        # Match any char that is not a digit, whitespace or hyphen (negative sign)
        pattern = re.compile(r'[^\d\s-]')

        if re.match(pattern, value) or not value:
            self.warning_message('Invalid Input', 'Input must be an integer')
            return ''
        else:
            if validate(eval(value)):
                return int(value)
            else:
                self.warning_message('Invalid Input', 'Input value does not match its conditions')
                return ''

    # Internal method to validate float numbers
    def _validate_float(self, value, validate=lambda x: True):
        assert isinstance(value, str), 'Value must be a string'
        assert callable(validate), 'File extensions validation must be a function'

        # Match any char that is not a digit, whitespace, dot or hyphen (negative sign)
        pattern = re.compile(r'[^\d\s\.\-]')

        if re.findall(pattern, value) or not value:
            self.warning_message('Invalid Input', 'Input must be a float')
            return ''
        else:
            if validate(eval(value)):
                try:
                    return float(value)
                except ValueError:
                    self.warning_message('Invalid Input', 'Input must be a float')
                    return ''
            else:
                self.warning_message('Invalid Input', 'Input value does not match its conditions')
                return ''



    def validate_cols(self, cols='', col_name=''):
        # Match any char that is not a digit, whitespace, comma or hyphen
        pattern = re.compile(r'[^\d\s,-]')
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

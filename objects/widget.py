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

    def validate_entry(self, entry=None, valid=lambda x: True, type_=None):
        assert isinstance(entry, str), 'Entry must be a string'
        assert isinstance(type_, list), 'Possible types must be given in a list'

        func = {
            'file': lambda x, y: self._validate_filepath(x, y),
            'range': lambda x, y: self._validate_range(x, y),
            'int': lambda x, y: self._validate_int(x, y),
            'float': lambda x, y: self._validate_float(x, y),
            'list': lambda x, y: self._validate_list(x, y),
            'str': lambda x, y: print('Not implemented yet!'),
        }
        ret = None
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
        if re.findall(pattern, value) or not value:
            self.warning_message('Invalid Input', 'Input must be an integer')
            return ''

        # Validate input as int
        if value.strip() and validate(eval(value)):
            try:
                return int(value)
            except ValueError:
                self.warning_message('Invalid Input', 'Input must be an integer')
                return ''
        else:
            self.warning_message('Invalid Input', 'Input value does not match its conditions')
            return ''

    # Internal method to validate float numbers
    def _validate_float(self, value, validate=lambda x: True):
        assert isinstance(value, str), 'Value must be a string'
        assert callable(validate), 'File extensions validation must be a function'

        # Match any char that is not a digit, whitespace, dot or hyphen (negative sign)
        pattern = re.compile(r'[^\d\s.\-]')
        if re.findall(pattern, value) or not value:
            self.warning_message('Invalid Input', 'Input must be a float')
            return ''

        # Validate input as float
        if value.strip() and validate(eval(value)):
            try:
                return float(value)
            except ValueError:
                self.warning_message('Invalid Input', 'Input must be a float')
                return ''
        else:
            self.warning_message('Invalid Input', 'Input value does not match its conditions')
            return ''

    def _validate_range(self, value, validate=lambda x: True):
        assert isinstance(value, str), 'Value must be a string'
        assert callable(validate), 'File extensions validation must be a function'

        # Match any char that is not a digit, whitespace or hyphen (negative sign)
        pattern = re.compile(r'[^\d\s\-]')
        if re.findall(pattern, value) or not value:
            self.warning_message('Invalid Input', 'Input must be a range (e.g. 1-4)')
            return ''

        for val in value.rsplit('-', 1):
            if not self._validate_int(val) and not validate(eval(val)):
                self.warning_message('Invalid Input', 'Input value does not match its conditions')
                return ''

        try:
            start, stop = map(eval, value.rsplit('-', 1))
            return range(start, stop + 1)
        except ValueError:
            self.warning_message('Invalid Input', 'Input value does not match its conditions')
            return ''

    def _validate_list(self, value, validate=lambda x: True):
        assert isinstance(value, str), 'Value must be a string'
        assert callable(validate), 'File extensions validation must be a function'

        # Match any char that is not a digit, whitespace or hyphen (negative sign)
        pattern = re.compile(r'[^\d\s\-,]')  # Maybe use this regex '\-?[\d\.]+' and change to `if not re.findall`
        if re.findall(pattern, value) or not value:
            self.warning_message('Invalid Input', 'Input must be a list (e.g. 1, 2, …)')
            return ''

        lst = []
        for val in value.split(','):
            if not (val.strip() and self._validate_int(val) and validate(val)):
                self.warning_message('Invalid Input', 'Input value does not match its conditions')
                return ''

            lst.append(int(val))

        return lst

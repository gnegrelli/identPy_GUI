from objects.widget import MyQWidget
from ui.ui_file_selection import Ui_file_selection


class file_selection(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_file_selection()

        super().__init__(parent)

        self.ui.find_path.clicked.connect(lambda: self.get_filepath())

    def get_filepath(self):
        print('Go find the file')

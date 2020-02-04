from objects.widget import MyQWidget
from ui.ui_initial_page import Ui_initialPage


class initial_page(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_initialPage()

        super().__init__(parent)

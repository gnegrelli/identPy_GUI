from objects import BaseWidget
from ui.ui_initial_page import Ui_initialPage


class initial_page(BaseWidget):
    def __init__(self, parent):

        self.ui = Ui_initialPage()

        super().__init__(parent)

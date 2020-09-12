from ui import InitialPage
from objects import BaseWidget


class initial_page(BaseWidget):

    def __init__(self, parent):

        self.ui = InitialPage()

        super().__init__(parent)

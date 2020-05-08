from objects import BaseWidget

from ui import InitialPage


class initial_page(BaseWidget):

    def __init__(self, parent):

        self.ui = InitialPage()

        super().__init__(parent)

from identpy_gui.ui import InitialPage
from identpy_gui.objects import BaseWidget


class initial_page(BaseWidget):

    def __init__(self, parent):

        self.ui = InitialPage()

        super().__init__(parent)

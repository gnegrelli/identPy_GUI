from objects.widget import MyQWidget
from ui.ui_initial_page import Ui_initialPage


class initial_page(MyQWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # Ui_initialPage().setupUi(self)

        self.ui = Ui_initialPage()
        self.ui.setupUi(self)

        self.ui.next_button.clicked.connect(lambda: self.next())

    def next(self):
        self.parent.setCurrentIndex(1)

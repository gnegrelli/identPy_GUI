from objects.widget import MyQWidget
from ui.ui_model_selection import Ui_model_selection


class model_selection(MyQWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_model_selection()
        self.ui.setupUi(self)

        self.ui.next.clicked.connect(lambda: self.next())
        self.ui.previous.clicked.connect(lambda: self.previous())

    def next(self):
        print(self.ui.selected_model.currentText())

    def previous(self):
        self.parent.setCurrentIndex(0)

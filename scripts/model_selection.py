from objects.widget import MyQWidget
from ui.ui_model_selection import Ui_model_selection


class model_selection(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_model_selection()

        super().__init__(parent)

    def next(self):
        print(self.ui.selected_model.currentText())
        super().next()

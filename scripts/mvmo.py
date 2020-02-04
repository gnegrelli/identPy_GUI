from objects.widget import MyQWidget
from ui.ui_mvmo import Ui_mvmo_setting


class mvmo(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_mvmo_setting()

        super().__init__(parent)

    def next(self):
        print(self.ui.max_gen.text())
        super().next()

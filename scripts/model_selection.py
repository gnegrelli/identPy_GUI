from objects.widget import MyQWidget
from ui.ui_model_selection import Ui_model_selection


class model_selection(MyQWidget):

    models = {
        'Spring-Mass': None,
        'Pendulum': None,
        'Linearized Z-IM Load': None,
        'DFIG': None,
    }

    def __init__(self, parent):

        self.ui = Ui_model_selection()

        super().__init__(parent)

    def next(self):
        print(self.ui.selected_model.currentText())
        super().next()

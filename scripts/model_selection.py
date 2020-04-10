from objects.widget import MyQWidget
from ui.ui_model_selection import Ui_model_selection

from identpy.Model import SpringMass, Pendulum, ZIM, DFIG


class model_selection(MyQWidget):

    models = {
        'Spring-Mass': SpringMass,
        'Pendulum': Pendulum,
        'Linearized Z-IM Load': ZIM,
        'DFIG': DFIG,
    }

    def __init__(self, parent):

        self.ui = Ui_model_selection()

        super().__init__(parent)

    def next(self):
        print(self.ui.selected_model.currentText())
        super().next()

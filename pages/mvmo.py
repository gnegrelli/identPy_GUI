from objects import MethodWidget

from ui import UI_MVMO

from identpy.Method import MVMO


class mvmo(MethodWidget):

    def __init__(self, parent):

        self.ui = UI_MVMO()

        super().__init__(parent)

        self.lower_bound = []
        self.upper_bound = []

        self.populate(self.parent.estimator.model.parameters.keys())

    def next(self):
        print(self.ui.max_gen.text())
        lower_bound = [lb.text() for lb in self.lower_bound]
        upper_bound = [ub.text() for ub in self.upper_bound]
        print(lower_bound)
        print(upper_bound)
        if self.parent.method1 is None:
            self.parent.method1 = MVMO
        else:
            self.parent.method2 = MVMO
        print(self.parent.method1, self.parent.method2)
        super().next()

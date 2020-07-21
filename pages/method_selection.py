from objects import BaseWidget, MethodWidget

from ui import MethodSelection

from pages.mvmo import mvmo
from pages.ts import ts_page


class method_selection(BaseWidget):

    methods = {
        'MVMO': mvmo,
        'PSO': None,
        'Trajectory Sensitivity': ts_page,
    }

    def __init__(self, parent):

        self.ui = MethodSelection()

        super().__init__(parent)

        self.ui.checkBox.clicked.connect(lambda: self.ui.method2.setEnabled(self.ui.checkBox.isChecked()))

    def next(self):
        while isinstance(self.parent.widget(3), MethodWidget):
            self.parent.removeWidget(self.parent.widget(3))

        try:
            self.parent.method1_view = self.methods[self.ui.method1.currentText()](self.parent)
        except TypeError:
            self.warning_message('Missing Method', '%s Method not implemented yet.' % self.ui.method1.currentText())
        else:
            self.parent.insertWidget(-2, self.parent.method1_view)

        if self.ui.checkBox.isChecked():
            try:
                self.parent.method2_view = self.methods[self.ui.method2.currentText()](self.parent)
            except TypeError:
                self.warning_message('Missing Method', '%s Method not implemented yet.' % self.ui.method2.currentText())
            else:
                self.parent.insertWidget(-2, self.parent.method2_view)

                self.parent.method1_view.ui.estimate.hide()
                self.parent.method2_view.ui.next.hide()
        else:
            self.parent.method1_view.ui.next.hide()

        super().next()

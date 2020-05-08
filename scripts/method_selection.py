from objects import BaseWidget

from ui import MethodSelection

from scripts.mvmo import mvmo


class method_selection(BaseWidget):

    methods = {
        'MVMO': mvmo,
        'PSO': None,
        'Trajectory Sensitivity': None,
    }

    def __init__(self, parent):

        self.ui = MethodSelection()

        super().__init__(parent)

        self.ui.checkBox.clicked.connect(lambda: self.ui.method2.setEnabled(self.ui.checkBox.isChecked()))

    def next(self):

        try:
            self.parent.method1_view = self.methods[self.ui.method1.currentText()](self.parent)
        except TypeError:
            self.warning_message('Missing Method', '%s Method not implemented yet.' % self.ui.method1.currentText())
        else:
            self.parent.addWidget(self.parent.method1_view)

        if self.ui.checkBox.isChecked():
            try:
                self.parent.method2_view = self.methods[self.ui.method2.currentText()](self.parent)
            except TypeError:
                self.warning_message('Missing Method', '%s Method not implemented yet.' % self.ui.method2.currentText())
            else:
                self.parent.addWidget(self.parent.method2_view)

        super().next()

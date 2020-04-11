from objects.widget import MyQWidget
from ui.ui_method_selection import Ui_method_selection

from scripts.mvmo import mvmo


class method_selection(MyQWidget):

    methods = {
        'MVMO': mvmo,
        'PSO': None,
        'Trajectory Sensitivity': None,
    }

    def __init__(self, parent):

        self.ui = Ui_method_selection()

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

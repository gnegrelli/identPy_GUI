from objects.widget import MyQWidget
from ui.ui_method_selection import Ui_method_selection


class method_selection(MyQWidget):
    def __init__(self, parent):

        self.ui = Ui_method_selection()

        super().__init__(parent)

        self.ui.checkBox.clicked.connect(lambda: self.ui.method2.setEnabled(self.ui.checkBox.isChecked()))

    def next(self):
        print(self.ui.method1.currentText())
        print(self.ui.checkBox.isChecked())
        print(self.ui.method2.currentText())
        super().next()

from PySide2.QtWidgets import QWidget


class MyQWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

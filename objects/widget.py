from PySide2.QtWidgets import QWidget


class MyQWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def next(self):
        self.parent.setCurrentIndex(self.parent.currentIndex() + 1)

    def previous(self):
        self.parent.setCurrentIndex(self.parent.currentIndex() - 1)

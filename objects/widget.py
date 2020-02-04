from PySide2.QtWidgets import QWidget


class MyQWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        assert hasattr(self, 'ui'), "Page must have UI"

        self.ui.setupUi(self)

        try:
            self.ui.next.clicked.connect(lambda: self.next())
        except AttributeError:
            pass

        try:
            self.ui.previous.clicked.connect(lambda: self.previous())
        except AttributeError:
            pass

    def next(self):
        self.parent.setCurrentIndex(self.parent.currentIndex() + 1)

    def previous(self):
        self.parent.setCurrentIndex(self.parent.currentIndex() - 1)

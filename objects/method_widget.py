from objects import BaseWidget

from PySide2.QtWidgets import QWidget


class MethodWidget(BaseWidget, QWidget):

    def __init__(self, parent):

        super().__init__(parent)

        print('Teste')

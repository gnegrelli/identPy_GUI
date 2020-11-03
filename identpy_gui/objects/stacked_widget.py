from PySide2.QtWidgets import QStackedWidget

from identpy.objects import Estimator

from identpy_gui.pages import initial_page, model_selection, method_selection, results


class MyStackedWidget(QStackedWidget):

    estimator = Estimator()
    method1 = None
    method2 = None
    model = None

    def __init__(self):
        super().__init__()

        self.setGeometry(230, 180, 900, 450)
        self.setWindowTitle('identPy v1.0')

        self.initial_page = initial_page(self)
        self.addWidget(self.initial_page)

        self.model_selection = model_selection(self)
        self.addWidget(self.model_selection)

        self.method_selection = method_selection(self)
        self.addWidget(self.method_selection)

        self.results = results(self)
        self.addWidget(self.results)

        self.currentChanged.connect(lambda _: self.currentWidget().on_focus())

        self.setCurrentIndex(0)

        self.show()

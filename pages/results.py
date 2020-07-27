import matplotlib.pyplot as plt

from blinker import signal
from threading import Thread

from objects import BaseWidget
from ui import Ui_results

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


class results(BaseWidget):
    def __init__(self, parent):
        self.ui = Ui_results()

        super().__init__(parent)

        fig = plt.figure()

        self.parent.estimator.add_figure(fig)

        canvas = FigureCanvas(fig)
        self.ui.tab_layout.addWidget(canvas)

        self.t = Thread(target=self.parent.estimator)

    def previous(self):
        try:
            self.parent.estimator.remove_method()
        except IndexError:
            raise IndexError('No method set')
        super().previous()

    def on_focus(self):
        self.t.start()

import time

from objects import BaseWidget

from ui import Ui_results

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class results(BaseWidget):
    def __init__(self, parent):
        self.ui = Ui_results()

        super().__init__(parent)

        fig = plt.figure()

        self.parent.estimator.add_figure(fig)

        static_canvas = FigureCanvas(fig)
        self.ui.tab_layout.addWidget(static_canvas)
        # self.addToolBar(NavigationToolbar(static_canvas, self))

    def on_focus(self):
        self.parent.estimator()

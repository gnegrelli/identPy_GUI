import matplotlib.pyplot as plt

from blinker import signal
from threading import Thread

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from identpy_gui.ui import Ui_results
from identpy_gui.objects import BaseWidget


class results(BaseWidget):
    def __init__(self, parent):
        self.ui = Ui_results()

        super().__init__(parent)

        fig = plt.figure()

        self.parent.estimator.add_figure(fig)

        canvas = FigureCanvas(fig)
        self.ui.tab_layout.addWidget(canvas)

        self.t = Thread(target=self.parent.estimator)

        signal('start_method').connect(self.method_started)
        signal('iteration').connect(self.update_iter)
        signal('solution_updated').connect(self.update_solution)
        signal('end_method').connect(self.method_ended)

    def previous(self):
        try:
            self.parent.estimator.remove_method()
        except IndexError:
            raise IndexError('No method set')
        super().previous()

    def on_focus(self):
        self.t.start()

    def method_started(self, sender, **kwargs):
        if self.ui.log.toPlainText():
            self.ui.log.append('')
        self.ui.log.append('--- {}'.format(sender.name))

    def method_ended(self, sender, **kwargs):
        self.ui.log.append('--- {} elapsed time: {:.2f} s'.format(sender.name, sender.elapsed_time))

    def update_iter(self, sender, **kwargs):
        self.ui.iter.setText(str(sender))
        log = '{},{:.6f}'.format(kwargs['counter'], kwargs['error'])
        for p in kwargs['p']:
            log += ',{:.5f}'.format(p)
        self.ui.log.append(log)

    def update_solution(self, sender, **kwargs):
        self.ui.p_values.setText(self.parent.estimator.model.__str__(title=False))

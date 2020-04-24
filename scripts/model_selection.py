from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)

from objects.widget import MyQWidget
from ui.ui_model_selection import Ui_model_selection
from scripts.file_selection import MyFileExplorer

from identpy.Model import SpringMass, Pendulum, ZIM, DFIG


class model_selection(MyQWidget):

    models = {
        'Spring-Mass': SpringMass,
        'Pendulum': Pendulum,
        'Linearized Z-IM Load': ZIM,
        'DFIG': DFIG,
    }

    def __init__(self, parent):

        self.ui = Ui_model_selection()

        super().__init__(parent)

        self.ui.selected_model.currentIndexChanged.connect(lambda: self.model_change())

        self.ui.find_path.clicked.connect(lambda: self.get_filepath())

    def get_filepath(self):
        # Use Pyside2 File Dialog - filepath come out weird
        # dialog = QtWidgets.QFileDialog()
        # self.parent.hide()
        # name = dialog.getOpenFileName(self, "Open File", "/home", "Text Files (*.csv *.txt *.dat)")
        # self.parent.show()
        # self.ui.path.setText(name[0])

        # Use MyFileExplorer
        self.file_browser = MyFileExplorer(self)

    def model_change(self):
        chosen_model = self.ui.selected_model.currentText()
        if chosen_model in self.models.keys():
            print(self.models[chosen_model].inputs)
            print(self.models[chosen_model].outputs)
            self.populate_input(self.models[chosen_model].inputs.keys())
        else:
            print('Model not found')

    def populate_input(self, inputs):
        self.clear_layout(self.ui.verticalLayout_2)
        for input in inputs:
            self.add_input_row(input)

    def add_input_row(self, name):

        horizontal_layout = QHBoxLayout()

        param_name = QLabel('{} :'.format(name))
        param_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        param_name.setFixedSize(QSize(40, 25))
        horizontal_layout.addWidget(param_name)

        lower_bound = QLineEdit()
        lower_bound.setMaximumSize(QSize(40, 25))
        horizontal_layout.addWidget(lower_bound)

        self.ui.verticalLayout_2.addLayout(horizontal_layout)

        pass

    def next(self):
        print(self.ui.selected_model.currentText())
        if self.ui.selected_model.currentText() in self.models.keys():
            self.parent.model = self.models[self.ui.selected_model.currentText()]
            super().next()
        else:
            self.warning_message('Invalid Model', 'Please select a valid model from the list')

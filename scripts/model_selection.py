import numpy as np
import matplotlib.pyplot as plt

from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)

from objects.widget import MyQWidget
from ui.ui_model_selection import Ui_model_selection
from scripts.file_selection import MyFileExplorer

from identpy.Model import SpringMass, Pendulum, ZIM, DFIG
from identpy.Model.Implicit_Methods import RK4
from identpy.Objects import Estimator


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

        self.inputs = []
        self.outputs = []
        self.states = []

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
            self.inputs = self.populate_entries(self.ui.verticalLayout_2, self.models[chosen_model].inputs.keys())
            self.outputs = self.populate_entries(self.ui.verticalLayout_6, self.models[chosen_model].outputs.keys())
            self.states = self.populate_entries(self.ui.verticalLayout_8, self.models[chosen_model].outputs.keys())
        else:
            print('Model not found')

    def populate_entries(self, layout, entries):
        self.clear_layout(layout)
        entries_list = []
        for entry in entries:
            entries_list.append(self.add_entry_row(layout, entry))
        return entries_list

    def add_entry_row(self, layout, name):

        horizontal_layout = QHBoxLayout()

        param_name = QLabel('{} :'.format(name))
        param_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        param_name.setFixedSize(QSize(40, 25))
        horizontal_layout.addWidget(param_name)

        entry = QLineEdit()
        entry.setMaximumSize(QSize(40, 25))
        entry.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        horizontal_layout.addWidget(entry)

        layout.addLayout(horizontal_layout)

        return entry

    def next(self):
        go_on = True

        model = None
        filepath = None
        u_cols = []
        y_cols = []
        x_0 = []

        # Validate selected model
        if self.ui.selected_model.currentText() in self.models.keys():
            model = self.models[self.ui.selected_model.currentText()]
        else:
            self.warning_message('Invalid Model', 'Please select a valid model from the list')
            go_on = False

        # Validate data file
        if go_on:
            filepath = self._validate_filepath(self.ui.path.text(),
                                               validate=lambda x: x.split('.')[-1] in ['csv', 'txt', 'dat'])
            if filepath is '':
                go_on = False

        # Validate input columns
        if go_on and self.inputs:
            for i in self.inputs:
                column = self._validate_int(i.text(), validate=lambda x: x > 0)
                if column is '':
                    go_on = False
                    break
                u_cols.append(column)

        # Validate output columns
        if go_on and self.outputs:
            for i in self.outputs:
                column = self._validate_int(i.text(), validate=lambda x: x > 0)
                if column is '':
                    go_on = False
                    break
                y_cols.append(column)

        # Validate initial values of states
        if go_on and self.states:
            for i in self.states:
                column = self._validate_float(i.text())
                if column is '':
                    go_on = False
                    break
                x_0.append(column)

        if go_on:
            # Retrieve input and output data from file
            u, y = Estimator.input_read(filepath, u_cols, y_cols)

            # Add model to Estimator object
            self.parent.estimator.add_model(model(np.array(x_0), u[0], u, RK4(u[0][0], u[-1][0])))

            # Add output measured to Estimator object
            self.parent.estimator.add_measures(y)

            super().next()

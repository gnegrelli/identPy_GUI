# identpy_gui

This repository contains the GUI application developed for **[identPy](https://github.com/gnegrelli/identPy)**, a 
framework for parameter estimation of nonlinear dynamic systems. This application was created using PySide2.

## Installation

Install the project requirements by executing the following command on the terminal:

```bash
$ pip install -r requirements.txt
```

## Page design

It is recommended to use Qt5 Designer tool in order to create new pages and modify existing ones. It can be installed by executing the following command:

```bash
$ sudo apt install qttools5-dev-tools
```

In order to convert the ui files into python code, use the following command on the terminal:

```bash
$ pyside2-uic ui_file.ui -o python_file.py
```

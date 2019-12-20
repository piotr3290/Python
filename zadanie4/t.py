# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel

from MainWindow import Poletko


class Ui_MainWindow(object):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def simulate_step(self):
        self.pol.simulate_round()
        self.update_label()

    def reset_simulation(self):
        self.pol.reset_sim()
        self.update_label()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 650)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("centralwidget")

        self.pol = Poletko(self.central_widget, self, 10)
        self.pol.setGeometry(QtCore.QRect(0, 50, 600, 600))
        self.pol.setObjectName("poletunio")

        self.push_button_step = QtWidgets.QPushButton(self.central_widget)
        self.push_button_step.setGeometry(QtCore.QRect(10, 10, 93, 40))
        self.push_button_step.setObjectName("step")
        self.push_button_step.clicked.connect(lambda: self.simulate_step())

        self.push_button_reset = QtWidgets.QPushButton(self.central_widget)
        self.push_button_reset.setGeometry(QtCore.QRect(100, 10, 93, 40))
        self.push_button_reset.setObjectName("reset")
        self.push_button_reset.clicked.connect(lambda: self.reset_simulation())

        self.label_alive_amount = QLabel(self.central_widget)
        self.label_alive_amount.setGeometry(QtCore.QRect(300, 10, 93, 40))
        self.label_alive_amount.setObjectName("alive_label")

        MainWindow.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.menubar.setObjectName("menubar")

        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)

        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")

        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")

        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")

        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_quit)

        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")

        self.menu_colour = QtWidgets.QMenu(self.menu_settings)
        self.menu_colour.setObjectName("menu_color")

        self.action_sheeps = QtWidgets.QAction(MainWindow)
        self.action_sheeps.setObjectName("action_sheeps")

        self.action_wolf = QtWidgets.QAction(MainWindow)
        self.action_wolf.setObjectName("action_wolf")

        self.action_meadow = QtWidgets.QAction(MainWindow)
        self.action_meadow.setObjectName("action_meadow")

        self.menu_colour.addAction(self.action_sheeps)
        self.menu_colour.addAction(self.action_wolf)
        self.menu_colour.addAction(self.action_meadow)

        MainWindow.setMenuBar(self.menubar)

        self.menu_settings.addAction(self.menu_colour.menuAction())
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_button_step.setText(_translate("MainWindow", "Step"))
        self.push_button_reset.setText(_translate("MainWindow", "Reset"))
        self.update_label()
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_quit.setText(_translate("MainWindow", "Quit"))
        self.action_sheeps.setText(_translate("MainWindow", "Sheeps"))
        self.action_wolf.setText(_translate("MainWindow", "Wolf"))
        self.action_meadow.setText(_translate("MainWindow", "Meeeadow"))
        self.menu_colour.setTitle(_translate("MainWindow", "Change colour"))
        self.menu_settings.setTitle(_translate("MainWindow", "Settings"))

    def update_label(self):
        self.label_alive_amount.setText("Alive sheeps: " + str(self.pol.simulation.get_alive_amount()))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

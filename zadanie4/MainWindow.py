from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QEventLoop, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QSlider, QActionGroup, QAction

from SimulationVisualization import VisualizationWidget


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()
        self.loop_flag = False
        self.tick_time = 500
        self.show()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(600, 650)
        self.setWindowIcon(QIcon("icon.ico"))

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")

        self.pol = VisualizationWidget(self.central_widget, self, 10)
        self.pol.setGeometry(QtCore.QRect(0, 50, 600, 600))
        self.pol.setObjectName("poletunio")

        self.push_button_step = QtWidgets.QPushButton(self.central_widget)
        self.push_button_step.setGeometry(QtCore.QRect(5, 5, 80, 40))
        self.push_button_step.setObjectName("step")
        self.push_button_step.clicked.connect(lambda: self.simulate_step())

        self.push_button_reset = QtWidgets.QPushButton(self.central_widget)
        self.push_button_reset.setGeometry(QtCore.QRect(90, 5, 80, 40))
        self.push_button_reset.setObjectName("reset")
        self.push_button_reset.clicked.connect(lambda: self.reset_simulation())

        self.push_button_start = QtWidgets.QPushButton(self.central_widget)
        self.push_button_start.setGeometry(QtCore.QRect(175, 5, 80, 40))
        self.push_button_start.setObjectName("start")
        self.push_button_start.clicked.connect(lambda: self.start_loop())

        self.label_alive_amount = QLabel(self.central_widget)
        self.label_alive_amount.setGeometry(QtCore.QRect(290, 5, 100, 40))
        self.label_alive_amount.setObjectName("alive_label")

        self.zoom_slider = QSlider(self.central_widget)
        self.zoom_slider.setOrientation(Qt.Horizontal)
        self.zoom_slider.setGeometry(QtCore.QRect(410, 5, 180, 40))
        self.zoom_slider.setFocusPolicy(Qt.StrongFocus)
        self.zoom_slider.setTickPosition(QSlider.TicksBothSides)
        self.zoom_slider.setTickInterval(10)
        self.zoom_slider.setSingleStep(1)
        self.zoom_slider.setValue(50)
        self.zoom_slider.valueChanged.connect(lambda: self.zooming())

        self.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.menubar.setObjectName("menubar")

        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.setMenuBar(self.menubar)

        self.action_open = QtWidgets.QAction(self)
        self.action_open.setObjectName("action_open")
        self.action_open.triggered.connect(lambda: self.read_from_json_file())

        self.action_save = QtWidgets.QAction(self)
        self.action_save.setObjectName("action_save")
        self.action_save.triggered.connect(lambda: self.save_to_json_file())

        self.action_quit = QtWidgets.QAction(self)
        self.action_quit.setObjectName("action_quit")
        self.action_quit.triggered.connect(lambda: self.close())

        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)

        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")

        self.menu_colour = QtWidgets.QMenu(self.menu_settings)
        self.menu_colour.setObjectName("menu_color")

        self.menu_time = QtWidgets.QMenu(self.menu_settings)
        self.menu_time.setObjectName("menu_time")
        self.group = QActionGroup(self.menu_time)
        time_values = ["0.5", "1.0", "1.5", "2.0"]
        for time_val in time_values:
            action = QAction(time_val, self.menu_time, checkable=True, checked=time_val == time_values[0])
            self.menu_time.addAction(action)
            self.group.addAction(action)
        self.group.setExclusive(True)
        self.group.triggered.connect(self.change_time)

        self.action_sheeps = QtWidgets.QAction(self)
        self.action_sheeps.setObjectName("action_sheeps")
        self.action_sheeps.triggered.connect(lambda: self.change_sheeps_colour())

        self.action_wolf = QtWidgets.QAction(self)
        self.action_wolf.setObjectName("action_wolf")
        self.action_wolf.triggered.connect(lambda: self.change_wolf_colour())

        self.action_meadow = QtWidgets.QAction(self)
        self.action_meadow.setObjectName("action_meadow")
        self.action_meadow.triggered.connect(lambda: self.change_meadow_colour())

        self.menu_colour.addAction(self.action_sheeps)
        self.menu_colour.addAction(self.action_wolf)
        self.menu_colour.addAction(self.action_meadow)

        self.setMenuBar(self.menubar)

        self.menu_settings.addAction(self.menu_colour.menuAction())
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.menu_time.menuAction())

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Wolf and sheeps"))
        self.push_button_step.setText(_translate("MainWindow", "Step"))
        self.push_button_reset.setText(_translate("MainWindow", "Reset"))
        self.push_button_start.setText(_translate("MainWindow", "Start"))
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
        self.menu_time.setTitle(_translate("MainWindow", "Time"))

    def update_label(self):
        self.label_alive_amount.setText("Alive sheeps: " + str(self.pol.simulation.get_alive_amount()))

    def simulate_step(self):
        self.pol.simulate_round()
        self.update_label()

    def reset_simulation(self):
        self.pol.reset_sim()
        self.update_label()

    def change_sheeps_colour(self):
        self.pol.set_sheeps_colour()

    def change_wolf_colour(self):
        self.pol.set_wolf_colour()

    def change_meadow_colour(self):
        self.pol.set_background_colour()

    def save_to_json_file(self):
        self.pol.save_file_json()

    def read_from_json_file(self):
        self.pol.open_file_json()

    def zooming(self):
        self.pol.set_zoom(self.zoom_slider.value())

    def enable_buttons(self, value):
        self.push_button_reset.setEnabled(value)
        self.push_button_step.setEnabled(value)
        self.menubar.setEnabled(value)

    def change_time(self, action):
        self.tick_time = 1000 * float(action.text())

    def start_loop(self):
        self.loop_flag = not self.loop_flag
        self.enable_buttons(not self.loop_flag)
        if self.loop_flag:
            self.push_button_start.setText("Stop")
        else:
            self.push_button_start.setText("Start")

        while self.pol.simulation.get_alive_amount() > 0 and self.loop_flag:
            self.simulate_step()
            loop = QEventLoop()
            QTimer.singleShot(self.tick_time, loop.quit)
            loop.exec_()

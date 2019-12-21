import random

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen, QBrush, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QColorDialog, QFileDialog
from chase.Simulation import Simulation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 900)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 801, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.button_1 = QPushButton(self.verticalLayoutWidget)
        self.button_1.setObjectName("guzior")
        self.verticalLayout.addWidget(self.button_1)

        self.poletko = Poletko(self.verticalLayoutWidget)
        self.poletko.initUI(10)
        self.verticalLayout.addWidget(self.poletko)

        """self.layout.addWidget(QPushButton("Step"))
        self.layout.addWidget(Poletko(10))"""
        self.show()


class Poletko(QWidget):
    def __init__(self, parent, logic, init_pos_limit):
        super(Poletko, self).__init__(parent)
        self.logic = logic
        self.setAutoFillBackground(True)
        """palette = QPalette()
        oImage = QImage("background.jpg")
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)"""

        self.init_pos_limit = init_pos_limit
        self.scale = 200 / init_pos_limit
        self.points = []
        self.wolf = QPoint(10, 10)
        self.sheepsColour = Qt.red
        self.wolfColour = Qt.blue
        self.backgroundColour = Qt.green
        self.setGeometry(QRect(0, 300, 600, 600))
        self.simulation = Simulation(sheeps_amount=0, init_pos_limit=init_pos_limit)
        self.show()

    def mouseReleaseEvent(self, e):
        if (abs(e.pos().x() - 600 / 2) <= (2 * 300 / 3)) & \
                (abs(e.pos().y() - 600 / 2) <= (2 * 300 / 3)):
            if e.button() == Qt.LeftButton:
                self.simulation.add_sheep((e.pos().x() - 300) / self.scale, (e.pos().y() - 300) / self.scale)
                self.logic.update_label()

            elif e.button() == Qt.RightButton:
                self.simulation.set_wolf_position((e.pos().x() - 300) / self.scale, (e.pos().y() - 300) / self.scale)
            self.update()

    def paintEvent(self, e):
        """palette = self.palette()
        palette.setColor(self.backgroundRole(), self.backgroundColour)
        self.setPalette(palette)"""
        palette = QPalette()
        oImage = QImage("background.jpg")
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        qp.end()

    def draw_points(self, qp):
        qp.setBrush(self.sheepsColour)
        qp.setPen(self.sheepsColour)
        for sheep in self.simulation.get_sheeps():
            if sheep.get_alive():
                qp.drawEllipse(sheep.get_x() * self.scale + 300, sheep.get_y() * self.scale + 300, 12, 12)
        qp.setBrush(self.wolfColour)
        qp.setPen(self.wolfColour)
        qp.drawEllipse(self.simulation.get_wolf().get_x() * self.scale + 300,
                       self.simulation.get_wolf().get_y() * self.scale + 300, 12, 12)

    def simulate_round(self):
        if not len(self.simulation.get_sheeps()):
            info_window = InfoWindow("There is no sheep!", self)
            info_window.show()
        else:
            self.simulation.simulate()
            self.update()
            if not self.simulation.get_alive_amount():
                info_window = InfoWindow("All sheeps have been devoured!", self)
                info_window.show()

    def reset_sim(self):
        self.simulation = Simulation(sheeps_amount=0, init_pos_limit=self.init_pos_limit)
        self.update()

    def setSheepsColour(self):
        self.sheepsColour = QColorDialog.getColor()
        self.update()

    def setWolfColour(self):
        self.wolfColour = QColorDialog.getColor()
        self.update()

    def setBackgroundColour(self):
        self.backgroundColour = QColorDialog.getColor()
        self.update()

    def save_file_json(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '.', "JSON (*.json)")
        print(file_name)
        if file_name[0] != '':
            self.simulation.save_to_json(file_name[0])

    def open_file_json(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '.', "JSON (*.json)")

        if file_name[0] != '':
            self.reset_sim()
            self.simulation.read_from_json(file_name[0])
            self.update()


class InfoWindow(QtWidgets.QMainWindow):
    def __init__(self, text, parent=None):
        super(InfoWindow, self).__init__(parent)
        self.resize(200, 150)
        self.info_label = QLabel(self)
        self.info_label.setGeometry(QtCore.QRect(0, 10, 200, 40))
        self.info_label.setObjectName("info_label")
        self.info_label.setText(text)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.push_button_ok = QtWidgets.QPushButton(self)
        self.push_button_ok.setGeometry(QtCore.QRect(60, 60, 40, 30))
        self.push_button_ok.setObjectName("ok_button")
        self.push_button_ok.setText("OK")
        self.push_button_ok.clicked.connect(lambda: self.close())


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    # poletko = Poletko(10)
    app.exec_()

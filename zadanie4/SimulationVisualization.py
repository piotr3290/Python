from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QColorDialog, QFileDialog, QMessageBox

from chase.Simulation import Simulation


class VisualizationWidget(QWidget):
    def __init__(self, parent, logic, init_pos_limit):
        super(VisualizationWidget, self).__init__(parent)
        self.logic = logic
        self.setAutoFillBackground(True)
        self.init_pos_limit = init_pos_limit
        self.zoom = 1
        self.scale = (300 * (2 / 3) * self.zoom / init_pos_limit)
        self.points = []
        self.sheepsColour = Qt.red
        self.wolfColour = Qt.blue
        self.backgroundColour = Qt.green
        self.setGeometry(QRect(0, 300, 600, 600))
        self.ellipseSize = 12
        self.simulation = Simulation(sheeps_amount=0, init_pos_limit=init_pos_limit)
        self.show()

    def mouseReleaseEvent(self, e):
        if (abs(e.pos().x() - 600 / 2) <= (2 * 300 / 3) * self.zoom) & \
                (abs(e.pos().y() - 600 / 2) <= (2 * 300 / 3) * self.zoom) and not self.logic.loop_flag:
            if e.button() == Qt.LeftButton:
                self.simulation.add_sheep((e.pos().x() - 300) / self.scale, (e.pos().y() - 300) / self.scale)
                self.logic.update_label()

            elif e.button() == Qt.RightButton:
                self.simulation.set_wolf_position((e.pos().x() - 300) / self.scale, (e.pos().y() - 300) / self.scale)
            self.update()

    def paintEvent(self, e):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), self.backgroundColour)
        self.setPalette(palette)
        """palette = QPalette()
        oImage = QImage("background.jpg")
        palette.setBrush(QPalette.Window, QBrush(oImage))"""
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
                qp.drawEllipse(sheep.get_x() * self.scale + 300 - self.ellipseSize * self.zoom / 2,
                               sheep.get_y() * self.scale + 300 - self.ellipseSize * self.zoom / 2,
                               self.ellipseSize * self.zoom, self.ellipseSize * self.zoom)
        qp.setBrush(self.wolfColour)
        qp.setPen(self.wolfColour)

        qp.drawEllipse(self.simulation.get_wolf().get_x() * self.scale + 300 - self.ellipseSize * self.zoom / 2,
                       self.simulation.get_wolf().get_y() * self.scale + 300 - self.ellipseSize * self.zoom / 2,
                       self.ellipseSize * self.zoom, self.ellipseSize * self.zoom)

    def simulate_round(self):
        if not len(self.simulation.get_sheeps()):
            QMessageBox.about(self, "Error", "There is no sheep!")
            # info_window = InfoWindow("There is no sheep!", self.logic)
            # info_window.show()
        else:
            self.simulation.simulate()
            self.update()
            if not self.simulation.get_alive_amount():
                QMessageBox.about(self, "Game over", "All sheeps have been devoured!")
                self.logic.start_loop()
                # info_window = InfoWindow("All sheeps have been devoured!", self.logic)
                # info_window.show()

    def reset_sim(self):
        self.simulation = Simulation(sheeps_amount=0, init_pos_limit=self.init_pos_limit)
        self.update()

    def set_sheeps_colour(self):
        sheeps_colour = QColorDialog.getColor()
        if sheeps_colour.isValid():
            self.sheepsColour = sheeps_colour
        self.update()

    def set_wolf_colour(self):
        wolf_colour = QColorDialog.getColor()
        if wolf_colour.isValid():
            self.wolfColour = wolf_colour
        self.update()

    def set_background_colour(self):
        background_colour = QColorDialog.getColor()
        if background_colour.isValid():
            self.backgroundColour = background_colour
        self.update()

    def save_file_json(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '.', "JSON (*.json)")
        if file_name[0] != '':
            self.simulation.save_to_json(file_name[0])

    def open_file_json(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '.', "JSON (*.json)")

        if file_name[0] != '':
            self.reset_sim()
            self.simulation.read_from_json(file_name[0])
            self.update()
            self.logic.update_label()

    def standardization(self, x, new_min, new_max, old_min, old_max):
        return (x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min

    def set_zoom(self, zoom):
        if zoom > 50:
            self.zoom = self.standardization(zoom, 1, 5, 50, 99)
        elif zoom < 50:
            self.zoom = self.standardization(zoom, 0.2, 1, 0, 50)
        self.scale = (300 * (2 / 3) * self.zoom / self.init_pos_limit)
        self.update()

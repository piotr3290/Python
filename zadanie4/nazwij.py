import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Poletko2(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 100, 100)
        self.show()

    def paintEvent(self, e):
        rysowanie = QPainter()
        rysowanie.begin(self)
        rysowanie.setPen(Qt.white)
        rysowanie.drawPoint(50, 50)
        for i in range(1000):
            x = random.randint(1, self.size.width() - 1)
            y = random.randint(1, self.size.height() - 1)
            rysowanie.drawPoint(x, y)
        rysowanie.end()


app = QApplication([])
app.setStyle('Fusion')
dark_palette = QPalette()

dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)

app.setPalette(dark_palette)
app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('gora'))
layout.addWidget(QPushButton('dol'))
poledorysowania = QWidget()

poletko = Poletko()
layout.addWidget(poletko)
window.setLayout(layout)
window.show()
app.exec_()

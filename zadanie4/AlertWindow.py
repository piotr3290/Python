from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class InfoWindow(QtWidgets.QMainWindow):
    def __init__(self, text, parent=None):
        super(InfoWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self.resize(200, 120)
        self.setWindowIcon(QtGui.QIcon("icon.ico"))

        self.info_label = QLabel(self)
        self.info_label.setGeometry(QtCore.QRect(0, 10, 200, 40))
        self.info_label.setObjectName("info_label")
        self.info_label.setText(text)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.push_button_ok = QtWidgets.QPushButton(self)
        self.push_button_ok.setGeometry(QtCore.QRect(80, 60, 40, 30))
        self.push_button_ok.setObjectName("ok_button")
        self.push_button_ok.setText("OK")
        self.push_button_ok.clicked.connect(lambda: self.close())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        self.menusdfghj = QtWidgets.QMenu(self.menubar)
        self.menusdfghj.setObjectName("menusdfghj")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actiondfghjkl = QtWidgets.QAction(MainWindow)
        self.actiondfghjkl.setObjectName("actiondfghjkl")

        self.actionfghjkl = QtWidgets.QAction(MainWindow)
        self.actionfghjkl.setObjectName("actionfghjkl")

        self.menusdfghj.addAction(self.actiondfghjkl)
        self.menusdfghj.addAction(self.actionfghjkl)

        self.menubar.addAction(self.menusdfghj.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menusdfghj.setTitle(_translate("MainWindow", "sdfghj"))
        self.actiondfghjkl.setText(_translate("MainWindow", "dfghjkl"))
        self.actionfghjkl.setText(_translate("MainWindow", "fghjkl"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

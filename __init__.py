import sys
import os
import PySide2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from MainWindow import Ui_MainWindow
from Controllers.TraySystem import TraySystem
from Controllers.Tools import Tools as tools

tools.configSongsPath()


windowStyle = """
    QMainWindow {
        background-image: url("assets/background.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(windowStyle)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

TraySystem(MainWindow, app).show()

sys.exit(app.exec())

import sys
from PyQt5 import QtWidgets
from views.Main import Ui_MainWindow
from Controllers.TraySystem import TraySystem


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

TraySystem(MainWindow, ui, app).show()

sys.exit(app.exec())

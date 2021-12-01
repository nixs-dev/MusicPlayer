import sys
from PyQt5 import QtWidgets
from views.Main import Ui_MainWindow
from Controllers.TraySystem import TraySystem

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

TraySystem(MainWindow, ui, app).show()

sys.exit(app.exec())

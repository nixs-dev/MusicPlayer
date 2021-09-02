from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functools import partial


class TraySystem(QSystemTrayIcon):
    def __init__(self, window, app):
        super().__init__(window)

        icon = QIcon("assets/icon.png")
        self.setIcon(icon)

        menu = QMenu()
        quit = menu.addAction('quit')
        quit.triggered.connect(partial(self.finishApplication, window, app))

        self.setContextMenu(menu)



    def finishApplication(self, window, app):
        app.quit()


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functools import partial


class TraySystem(QSystemTrayIcon):

    applicationClass = None

    def __init__(self, window, application_class, app):
        super().__init__(window)
        self.applicationClass = application_class

        icon = QIcon("assets/icon.png")
        self.setIcon(icon)

        menu = QMenu()
        openPlayerWinow = menu.addAction('Open')
        quit = menu.addAction('Quit')
        nextSong = menu.addAction('Next')
        previousSong = menu.addAction('Previous')

        openPlayerWinow.triggered.connect(partial(self.showWindow, window))
        nextSong.triggered.connect(partial(self.toNextSong))
        previousSong.triggered.connect(partial(self.toPreviousSong))
        quit.triggered.connect(partial(self.finishApplication, window, app))

        self.setContextMenu(menu)

    def showWindow(self, window):
        window.show()

    def toNextSong(self):
        currentSound = self.applicationClass.songs.index(self.applicationClass.selected_song)
        self.applicationClass.next_song(currentSound)

    def toPreviousSong(self):
        currentSound = self.applicationClass.songs.index(self.applicationClass.selected_song)
        self.applicationClass.previous_song(currentSound)

    def finishApplication(self, window, app):
        app.quit()



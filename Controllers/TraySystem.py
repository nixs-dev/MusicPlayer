from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functools import partial


class TraySystem(QSystemTrayIcon):

    applicationClass = None

    def __init__(self, window, applicationClass, app):
        super().__init__(window)
        self.applicationClass = applicationClass

        icon = QIcon("assets/icon.png")
        self.setIcon(icon)

        menu = QMenu()
        quit = menu.addAction('Quit')
        nextSong = menu.addAction('Next')
        previousSong = menu.addAction('Previous')

        nextSong.triggered.connect(partial(self.toNextSong))
        previousSong.triggered.connect(partial(self.toPreviousSong))
        quit.triggered.connect(partial(self.finishApplication, window, app))

        self.setContextMenu(menu)


    def toNextSong(self):
        currentSound = self.applicationClass.songs.index(self.applicationClass.selected_song)
        self.applicationClass.nextSong(currentSound)

    def toPreviousSong(self):
        currentSound = self.applicationClass.songs.index(self.applicationClass.selected_song)
        self.applicationClass.previousSong(currentSound)

    def finishApplication(self, window, app):
        app.quit()



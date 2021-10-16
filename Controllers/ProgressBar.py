from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)


class ProgressBar(QThread):
    mode = 'toNext'
    threadSignal = pyqtSignal(int)
    setDurationSignal = pyqtSignal(int)
    finishedSignal = pyqtSignal(str)
    quit = [False, 'finished']
    player = None
    duration = 0
    position = 0
    
    def __init__(self, player):
        super(ProgressBar, self).__init__()

        self.player = player

    def main_loop(self):
        while self.position < self.duration:
            if self.quit[0]:
                break

            print()
            self.position = self.player.position()/1000
            self.threadSignal.emit(self.position)

    def run(self):
        while self.duration == 0:
            if self.player.durationChanged:
                self.setDurationSignal.emit(self.player.duration()/1000)

        self.position = self.player.position()/1000
        
        self.main_loop()

        if self.quit[1] == 'finished':
            self.finishedSignal.emit(self.mode)
            
    def set_player_position(self, pos):
        self.player.setPosition(pos*1000)

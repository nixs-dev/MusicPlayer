import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M


class AudioPlayer(M.QMediaPlayer):
    prefixPath = './songs/'
    song = ''
    player = None

    def __init__(self, song):
        super().__init__()
        self.song = song

        url = C.QUrl.fromLocalFile(self.prefixPath + self.song)
        content = M.QMediaContent(url)
        self.setMedia(content)


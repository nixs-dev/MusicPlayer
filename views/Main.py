# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from Controllers.AudioPlayer import AudioPlayer as player
from Controllers.Tools import Tools as tools
from Controllers.ProgressBar import ProgressBar
from Controllers.Styler import Styler
from functools import partial


class Ui_MainWindow(object):
    playOrPausedIcon = ['||', '►']
    onBackground = False
    selected_song = ''
    currentSound = None
    soundProgress = None
    barIsSelected = False
    paused = False
    repeat = False
    songs = []

    def show_songs(self):
        for song in self.songs:
            musicName = QtWidgets.QLabel(song)
            musicName.mousePressEvent = partial(self.selected_item, song)
            musicName.enterEvent = partial(Styler.song_on_mouse_over, musicName)
            musicName.leaveEvent = partial(Styler.song_on_mouse_leave, musicName)
            musicName.setStyleSheet("margin-left: 4px; border: none; color: #000000")
            musicName.setCursor(QtCore.Qt.PointingHandCursor)
            self.verticalLayout.addWidget(musicName)

    def next_song(self, actualSongIndex):
        try:
            _next = self.songs[actualSongIndex + 1]
        except:
            _next = self.songs[0]

        self.selected_item(_next, None)

    def previous_song(self, actualSongIndex):
        try:
            _previous = self.songs[actualSongIndex - 1]
        except:
            _previous = self.songs[len(self.songs)-1]

        self.selected_item(_previous, None)

    def selected_item(self, text, event):
        self.selected_song = text

        if self.currentSound == None:
            self.currentSound = player(self.selected_song, self.musicVolume.value())
        else:
            self.currentSound.stop()
            self.currentSound = player(self.selected_song, self.musicVolume.value())
        
        if self.soundProgress is not None:
            self.soundProgress.quit = [True, 'changed']

        self.config_player()
        self.sound_unready()

    def config_player(self):
        self.soundProgress = ProgressBar(self.currentSound)
        self.soundProgress.mode = 'repeat' if self.repeat else 'toNext'
        self.soundProgress.threadSignal.connect(self.update_progress_bar)
        self.soundProgress.setDurationSignal.connect(self.sound_ready)
        self.soundProgress.finishedSignal.connect(self.song_finished)
        self.soundProgress.start()
        self.soundProgress.exec()

    def start(self):
        self.currentSound.play()
        self.playSongButton.setText(self.playOrPausedIcon[0])

    def pause_or_play(self):
        if self.currentSound.state() == QMediaPlayer.PlayingState:
            self.currentSound.pause()
            self.playSongButton.setText(self.playOrPausedIcon[1])
        else:
            self.currentSound.play()
            self.playSongButton.setText(self.playOrPausedIcon[0])

    def song_finished(self, typeFinish):
        self.playSongButton.setText(self.playOrPausedIcon[1])
        self.currentSound.setPosition(0)
        self.horizontalSlider.setValue(0)
        self.currentSound.stop()

        if typeFinish == 'toNext':
            self.next_song(self.songs.index(self.selected_song))
        elif typeFinish == 'repeat':
            self.selected_item(self.selected_song, None)

    def update_progress_bar(self, value):
        if not self.barIsSelected:
            self.horizontalSlider.setValue(value)

    def sound_ready(self, _time):
        self.playSongButton.setEnabled(True)
        self.horizontalSlider.setEnabled(True)
        self.loopIcon.setEnabled(True)
        self.musicVolume.setEnabled(True)

        self.musicDuration.setText(tools.number_to_time(_time))
        self.soundProgress.duration = _time
        self.horizontalSlider.setMaximum(_time)
        self.playSongButton.setText(self.playOrPausedIcon[1])
        self.musicName.setText(self.selected_song)
        self.horizontalSlider.setValue(0)

        self.start()

    def sound_unready(self):
        self.playSongButton.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.loopIcon.setEnabled(False)
        self.musicVolume.setEnabled(False)

        self.musicDuration.setText('00:00')
        self.soundProgress.duration = 1
        self.horizontalSlider.setMaximum(1)
        self.playSongButton.setText(self.playOrPausedIcon[1])
        self.musicName.setText('')
        self.horizontalSlider.setValue(0)

    def on_mouse_press(self, name, elem, event):
        if name == "loopIcon":
            self.repeat = True if not self.repeat else False
            elem.setStyleSheet("border: none; color: #0000FF")
            self.soundProgress.mode = 'repeat' if self.repeat else 'toNext'
    
    def on_press_bar(self):
        self.barIsSelected = True

    def on_drag_bar(self, pos):
        self.barIsSelected = True
        self.soundProgress.set_player_position(pos)

    def on_leave_bar(self):
        self.barIsSelected = False

    def close_event(self, event):
        try:
            if self.currentSound.state() == QMediaPlayer.PlayingState:
                self.window.hide()
                event.ignore()
            else:
                event.accept()
        except AttributeError:
            event.accept()

    def on_volume_bar_drag(self, value):
        self.currentSound.setVolume(value)

    def load_background(self):
        image_background = QtGui.QImage("assets/background.jpg")

        scaled_image = image_background.scaled(QtCore.QSize(1034, 700))
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(scaled_image))
        self.window.setPalette(palette)

    def setupUi(self, MainWindow):
        self.window = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 700)
        MainWindow.setFixedSize(1024, 700)
        MainWindow.closeEvent = partial(self.close_event)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 280, 251, 410))
        self.scrollArea.setStyleSheet("background-color: #FFFFFF; border: 4px ridge black")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 410))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: #FFFFFF; border: none")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 410))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(400, 280, 561, 410))
        self.widget.setStyleSheet("background-color: #FFFFFF; border: 4px ridge black; border-radius: 10px")
        self.widget.setObjectName("widget")
        self.discPicture = QtWidgets.QLabel(self.widget)
        self.discPicture.setGeometry(150, 10, 250, 200)
        self.discPicture.setPixmap(QtGui.QPixmap('assets/discPicture.jpg'))
        self.discPicture.setScaledContents(True)
        self.musicName = QtWidgets.QLabel(self.widget)
        self.musicName.setGeometry(QtCore.QRect(10, 210, 531, 51))
        self.musicName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.musicName.setStyleSheet("color: rgb(150, 74, 255);\n"
"font: 87 11pt \"Arial Black\"; border: none")
        self.musicName.setTextFormat(QtCore.Qt.AutoText)
        self.musicName.setAlignment(QtCore.Qt.AlignCenter)
        self.musicName.setObjectName("musicName")
        self.musicVolume = QtWidgets.QSlider(QtCore.Qt.Vertical, self.widget)
        self.musicVolume.setEnabled(False)
        self.musicVolume.setMaximum(100)
        self.musicVolume.setValue(50)
        self.musicVolume.setGeometry(QtCore.QRect(20, 150, 10, 100))
        self.musicVolume.setStyleSheet('background-color: None; border: None')
        self.musicVolume.sliderMoved.connect(self.on_volume_bar_drag)
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 280, 491, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setStyleSheet("border: none")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.sliderPressed.connect(self.on_press_bar)
        self.horizontalSlider.sliderMoved.connect(self.on_drag_bar)
        self.horizontalSlider.sliderReleased.connect(self.on_leave_bar)
        self.musicDuration = QtWidgets.QLabel(self.widget)
        self.musicDuration.setGeometry(QtCore.QRect(510, 280, 31, 16))
        self.musicDuration.setStyleSheet("color: #000000; border: none")
        self.musicDuration.setObjectName("musicDuration")
        self.loopIcon = QtWidgets.QLabel(self.widget)
        self.loopIcon.setEnabled(False)
        self.loopIcon.setGeometry(QtCore.QRect(510, 310, 31, 20))
        self.loopIcon.setObjectName("loopIcon")
        self.loopIcon.setStyleSheet("border: none; color: #000000")
        self.loopIcon.enterEvent = partial(Styler.loop_on_mouse_over, self.loopIcon, self.repeat)
        self.loopIcon.leaveEvent = partial(Styler.loop_on_mouse_leave, self.loopIcon, self.repeat)
        self.loopIcon.mousePressEvent = partial(self.on_mouse_press, 'loopIcon', self.loopIcon)
        self.loopIcon.setFont(QtGui.QFont('Arial', 15))
        self.playSongButton = QtWidgets.QPushButton(self.widget)
        self.playSongButton.setEnabled(False)
        self.playSongButton.setGeometry(QtCore.QRect(240, 340, 80, 40))
        self.playSongButton.setStyleSheet("border: none")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playSongButton.setFont(font)
        self.playSongButton.setStyleSheet("color: #000000;border: 1px solid;\n"
"border-radius: 10px;")
        self.playSongButton.clicked.connect(self.pause_or_play)
        self.playSongButton.setObjectName("playSongButton")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_background()
        self.songs = tools.get_songs()
        self.show_songs()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.musicDuration.setText(_translate("MainWindow", "00:00"))
        self.loopIcon.setText(_translate("MainWindow", "⟲"))
        self.playSongButton.setText(_translate("MainWindow", "►"))
        self.musicName.setText(_translate("MainWindow", "Nothing selected"))

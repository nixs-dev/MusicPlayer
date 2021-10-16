import os
import math


class Tools:

    default_songs_path = '/songs'
    appPath = os.getcwd().replace('/Tools', '')

    def get_songs():
        songs = os.listdir(Tools.appPath + Tools.default_songs_path)
        return songs

    def number_to_time(num):
        if num > 60:
            mins = math.floor(num/60)
            num -= 60 * mins
            seconds = num
        else:
            mins = 0
            seconds = num

        mins = str(mins)
        seconds = str(seconds)

        if len(mins) == 1:
            mins = '0' + mins
        if len(seconds) == 1:
            seconds = '0' + seconds

        result = mins + ':' + seconds

        return result

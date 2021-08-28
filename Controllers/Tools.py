import os
import math

class Tools:
	defaultSongsPath = '/songs'
	appPath = os.getcwd().replace('/Tools', '')
	main_path = ''

	def getSongs():
		return os.listdir(Tools.appPath + Tools.main_path)

	def configSongsPath():
		try:
			Tools.main_path = os.environ['SONGS_PATH']
		except:
			Tools.main_path = ''


		if Tools.main_path == '':
			os.environ['SONGS_PATH'] = Tools.defaultSongsPath
			Tools.main_path = Tools.defaultSongsPath
		elif os.environ['SONGS_PATH'][0] != '/':
			os.environ['SONGS_PATH'] = '/' + os.environ['SONGS_PATH']
			Tools.main_path = os.environ['SONGS_PATH']

		if not os.path.isdir(Tools.appPath + Tools.main_path):
			os.mkdir(Tools.appPath + Tools.main_path)


	def numberToTime(num):
		if num > 60:
			mins = math.floor(num/60)
			num -= 60 * mins
			seconds = num
		else:
			mins = 0
			seconds = num

		mins = str(mins)
		seconds = str(seconds)

		if(len(mins) == 1):
			mins = '0' + mins
		if(len(seconds) == 1):
			seconds = '0' + seconds

		result = mins + ':' + seconds

		return result

import os
from sys import platform


def _extension():
	if platform == "linux" or platform == "linux2":
		return ""  #linux2
	elif platform == "darwin":
		return ""  # OS X
	elif platform == "win32":
		return ".exe"  # Windows...


# get directory in which python script and webdriver are and 
# get the right format for chrome webdriver
DRIVER_PATH = os.path.join(os.getcwd(), ('chromedriver' + _extension())) 

path = 'rates.csv'
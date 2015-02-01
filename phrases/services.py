import subprocess
import os
from phrases.models import Phrase, Color

def ScrollrDisplay():
	os.system('sudo service marquee restart')
	#subprocess.call(['sudo', 'service', ' marquee', 'restart'])
	#subprocess.Popen(['sudo','service','marquee','restart'])
	#return True

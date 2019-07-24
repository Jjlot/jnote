import os
import syslog
import random

path = "/home/pi/Desktop/nfs/newMovie/"
# path = "/home/pi/Desktop/clannad/"

prelog = '[Player]'

syslog.syslog(prelog + 'Start')

files = os.listdir(path)
s = []

for file in files:
    if not os.path.isdir(file):
        # print file
        s.append(file)


# print s

# Set random
r = random.sample(s, len(s))
print r

for file in r:
	cmd = "vlc " + path + file + " -f"
	print cmd
	os.system(cmd)	
	# os.system("vlc -f " + path + file)


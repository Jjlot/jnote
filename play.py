import os
import syslog
import random



prelog = '[Player]'

syslog.syslog(prelog + 'Start')

path0 = "/home/pi/Desktop/nfs/"
# path0 = "/home/media/"

continus = ['Anime', 'documentary_file', 'teleplay']
randplay = ['movie', 'mv', 'video']
high_freq= ['high_freq']

s = []
for dirname in continus:
	print dirname
	g = os.walk(path0 + dirname)
	for path,dir_list,file_list in g:
		for dir_name in dir_list:
			s.append(os.path.join(path, dir_name))

for dirname in randplay:
	g = os.walk(path0 + dirname)
	for path,dir_list,file_list in g:
		for file_name in file_list:
			s.append(os.path.join(path, file_name))

i = 0
while i < 3:
	i += 1
	for dirname in high_freq:
		g = os.walk(path0 + dirname)
		for path,dir_list,file_list in g:
			for file_name in file_list:
				s.append(os.path.join(path, file_name))


r = random.sample(s, len(s))

for file in r:
        # cmd = "vlc \"" + file + "\" -f --video-title-show --video-title-position 6 --video-title-timeout 0x7FFFFFFF"
	cmd = "vlc \"" + file + "\" -f"

	print cmd
	syslog.syslog(prelog + cmd)
	os.system(cmd)	


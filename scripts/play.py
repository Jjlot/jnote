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
while i < 10:
	i += 1
	for dirname in high_freq:
		g = os.walk(path0 + dirname)
		for path,dir_list,file_list in g:
			for file_name in file_list:
				s.append(os.path.join(path, file_name))


r = random.sample(s, len(s))

for file in r:
	cmd = "vlc " + file + " -f"
	print cmd
	syslog.syslog(prelog + cmd)
	os.system(cmd)	




exit()


path = "/home/pi/Desktop/nfs/newMovie/"
# path = "/home/pi/Desktop/clannad/"

# Anime  documentary_film  movie  movie_todo  mv  newMovie  teleplay  video


prelog = '[Player]'

syslog.syslog(prelog + 'Start')

g = os.walk(r"/home/media/")
s = []
d = []

for path,dir_list,file_list in g:
	for file_name in file_list:
		# print(os.path.join(path, file_name))
		s.append(os.path.join(path, file_name))
	for dir_name in dir_list:
		d.append(os.path.join(path, dir_name))
		print dir_name
# print d

# for dir in d:

	# print dir

exit()

r = random.sample(s, len(s))

for file in r:
	cmd = "vlc " + path + file + " -f"
	print cmd
	# os.system(cmd)	
	# os.system("vlc -f " + path + file)


exit()


files = os.listdir(path)

for file in files:
    if not os.path.isdir(file):
        # print file
        s.append(file)


# print s

# Set random
r = random.sample(s, len(s))
print r



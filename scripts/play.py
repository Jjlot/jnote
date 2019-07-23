import os
import syslog
import random

path = "/home"

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
print random.sample(s, len(s))

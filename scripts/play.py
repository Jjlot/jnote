import os
path = "/home"

files = os.listdir(path)
s = []

for file in files:
    if not os.path.isdir(file):
        # print file
        s.append(file)


print s

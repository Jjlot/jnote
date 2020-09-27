import os
import syslog
import random
import time
import getopt
import sys

directory = "/home/"
debug_mode = False
nfs_ip = "192.168.0.102"
nfs_dir = "/media/slot3_4t/media"
local_dir = "/home/pi/Desktop/nfs"

def mount_nfs():
    # Mount nfs
    print(" Mounting nfs")
    while os.system("mount | grep " + local_dir) != 0 :
        os.system("sudo mount -t nfs " + nfs_ip + ":" + nfs_dir + " " + local_dir)
        time.sleep(5)

def _play(file_name):
    print(" File play: " + file_name)

    """
    # cmd = "vlc \"" + file + "\" -f --video-title-show --video-title-position 6 --video-title-timeout 0x7FFFFFFF"
    cmd = "vlc \"" + file + "\" -f --play-and-exit"

    print(cmd)
    syslog.syslog(prelog + cmd)
    os.system(cmd)
    """

# Play a path or file
def play(path):
    print(" I'm playing: " + path)

    if os.path.isfile(path):
        print(" It's a file")
        _play(path)

    else:
        print(" It's a directory")
        files = os.listdir(path)

        for file in files:
            abs_path = path + "/" + file
            _play(abs_path)

def get_list(path):
    for file in os.listdir(path):
        abs_file = path + "/" + file
        if os.path.isfile(abs_file):
            file_list.append(abs_file)

def main():

    mount_nfs()

    prelog = '[Player]'

    syslog.syslog(prelog + 'Start')

    path0 = "/home/pi/Desktop/nfs/"
    # path0 = "/home/media/"

    continus = ['Anime', 'documentary_file', 'teleplay']
    randplay = ['movie', 'mv', 'video']
    high_freq= ['high_freq']

    s = []
    for dirname in continus:
        print(dirname)
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
        cmd = "vlc \"" + file + "\" -f --play-and-exit"

        print(cmd)
        syslog.syslog(prelog + cmd)
        os.system(cmd)

if __name__ == '__main__':

    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-d',['help','filename=','debug'])
    # print(opts)
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            print("[*] Help info")
        if opt_name in ('-d','--debug'):
            print(" Debug mode ")
            debug_mode = True

        if opt_name in ('-f','--filename'):
            fileName = opt_value
            print("[*] Filename is ",fileName)
            # do something

    mount_nfs()

    test_path = "/home/pi/Desktop/nfs/Anime/CLANNAD"
    play(test_path)

    # main()






import os
import syslog
import random
import time
import getopt
import sys

run_mode = 'local'
# run_mode = 'remote'
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
def start_play(path):
    print(" Walking in path: " + path)

    droots = os.listdir(path)
    for droot in droots:
        # movie, anime ...
        print(" Scan directory: " + droot) 

        d1s = os.listdir(droot)
        for d1 in d1s:
            if os.path.isfile(d1):
                print(" It's a file")
                _play(d1)

            else:
                print(" It's a directory")
                files = os.listdir(d1)

                for file in files:
                    abs_path = d1 + "/" + file
                    _play(abs_path)



def get_list(path_in):
    file_list = []

    for file_name in os.listdir(path_in):
        abs_file = path_in + "/" + file_name
        if os.path.isfile(abs_file):
            file_list.append(abs_file)

    g = os.walk(path_in)
    for path,dir_list,file_list in g:
        for dir_name in dir_list:
            # s.append(os.path.join(path, dir_name))
            print(dir_name)

    for file in file_list:
        print("aaaa")
        # print(file)


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

    if run_mode == 'remote':
        mount_nfs()

    test_path = "/home/src/jnote/test"
    print(test_path)

    start_play(test_path)
    """
    mount_nfs()

    test_path = "/home/pi/Desktop/nfs/Anime/CLANNAD"
    play(test_path)

    test_path = "/home/src/jnote/test"
    get_list(test_path)
    """

    # main()






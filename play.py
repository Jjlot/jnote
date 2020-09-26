import os
import syslog
import random
import time
import getopt
import sys

def mount_nfs():
    # Mount nfs
    print(" Mounting nfs")
    while os.system("mount | grep Desktop") != 0 :
        os.system("sudo mount -t nfs 10.0.0.102:/media/slot3_4t/media /home/pi/Desktop/nfs")
        time.sleep(5)

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

    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v',['help','filename=','version'])
    print(opts)
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            print("[*] Help info")
            sys.exit()
        if opt_name in ('-v','--version'):
            print("[*] Version is 0.01 ")
            sys.exit()
        if opt_name in ('-f','--filename'):
            fileName = opt_value
            print("[*] Filename is ",fileName)
            # do something

    # main()






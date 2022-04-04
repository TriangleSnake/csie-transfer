from typing import Type
import sys
import os
import subprocess
try:
        sys.argv[1]
        try:
            sys.argv[2]
        except:
            print("No dict file!")
            os.system("pause")
            exit()
except:
    print ("No RAR file!")
    os.system("pause")
    exit()
try:
    f=open(sys.argv[2],'r')
except:
    print ("Wrong dict directoin!")
    os.system('pause')
    exit()
while 1 :
    pwd=str(f.readline().strip('\n'))
    if pwd=='':
        print ('\033[1m'+'\033[91m'+'Password NOT match!'+'\033[0m')
        os.system("pause")
        exit()

    
    command='echo '+pwd+'|unrar x '+sys.argv[1]+'>nul 2>nul'
    crack_status=os.system(command)
    print ('\r\033[1m'+'\033[93m'+'trying '+pwd+'\033[0m',end='')
    if (crack_status)==0:
        string='Password found:'+pwd
        print ('\033[1m'+'\033[92m'+string)
        print ('\033[1m'+'Decompressed!'+'\033[0m')
        os.system('pause')
        exit()

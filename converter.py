from email.mime import base
import sys
try:
    mode=sys.argv[1]
except:
    print('mode? ex:hex to dec')
    mode=input()
num=input().split()
mode=mode.split(' ')
f=''
match mode[0]:
    case "hex":
        f='0x'
    case "bin":
        f='0b'
    case "oct":
        f='0o'
    case "ascii":
        for i in range(len(num)):
            num[i]=ord(num[i])
for i in range(len(num)):
    num[i]=f+num[i]
    num[i]=int(num[i],0)
match mode[2]:
    case "hex":
        for i in num:
            print(hex(i),end=' ')
    case "dec":
        for i in num:
            print(i,end=' ')
    case "oct":
        for i in num:
            print(oct(i),end=' ')
    case "bin":
        for i in num:
            print(bin(i),end=' ')
    case "ascii":
        for i in num:
            print(chr(i),end='')
        print('')
        for i in num:
            print(chr(i),end=' ')


        
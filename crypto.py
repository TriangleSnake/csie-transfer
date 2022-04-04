f=open("wordlist.txt",'r')
fc=open('wordlistcomp.txt','w')
lst=f.readlines()
total=len(lst)
now=0
for line in lst:
    nline=line
    num=0
    for i in range(len(line)):
        try:
            int(nline[i])
        except:
            num+=1
            nline=nline.replace(nline[i],str(num))
    fc.write(nline+'\n')
    print("\r"+"Writing "+str(now/total*100)+"%     ",end='')
    now+=1
fc.close()
        
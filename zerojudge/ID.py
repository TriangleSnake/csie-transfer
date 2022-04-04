ID=input()
num=ID[1:]
check=ord(ID[0])-55
if ID[0]=='W':
    check=32
elif ID[0]=='X':
    check=30
elif ID[0]=='Y':
    check=31
elif ID[0]>"H" and ID[0]<'O':
    check-=1
elif ID[0]=='I':
    check=34
elif ID[0]=='O':
    check=35
elif ID[0]>'O' and ID[0]<'W':
    check-=2
check=(check%10)*9+check//10
for i in range(len(num)):
    check+=(int(num[i]))*(8-i)
check+=int(ID[9])
if check%10==0:
    print("real")
else :
    print("fake")
    

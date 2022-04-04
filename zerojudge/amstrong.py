


def fnd(n,p):
    if n>=10:
        return (n%10)**p+fnd(n//10,p)
    else :
        return n**p
num=input().split(' ')
flag=False
for i in range(int(num[0]),int(num[1])+1):
    if i==fnd(i,len(str(i))):
        print(i,end=' ')
        flag=True
if flag==False:
    print("none")

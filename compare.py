a=open('C://Users/user/Desktop/a.txt','r',encoding="utf-8")
a=a.readlines()
b=open('C://Users/user/Desktop/b.txt','r',encoding="utf-8")
b=b.readlines()
for i in a:
    flag=False
    for j in b:
        if i==j:
            flag=True
    if flag==False:
        print(i,end='')

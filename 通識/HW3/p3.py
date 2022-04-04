#p3
from operator import truediv


num=input("請輸入數字範圍(例:2 500)").split()
flag=True
for i in range(eval(num[0]),eval(num[1])):
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            flag=False
            break
    if flag==True:
        print(i,end=' ')
    flag=True
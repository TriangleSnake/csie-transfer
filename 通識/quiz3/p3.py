#p3
import string


string=''
def sum(n):
    if n==1:
        return 1
    else :
        return n*(sum(n-1))
        
n=eval(input("請輸入 n 的值:"))
if n<0:
    print("負數沒有階乘!")
elif n==0:
    print("階乘為:0")
    print("總合為:1")
else:
    for i in range(1,n):
        string+=str(i)
        string+='*'
    string+=str(n)
    print("階乘為:",string)
    print("總合為:",sum(n))


#5-1
a=eval(input("請輸入a的值:"))
b=eval(input("請輸入b的值:"))
print(a,end='')
if a>b:
    print(">",end='')
elif a<b:
    print("<",end='')
else:
    print("=",end='')
print(b)
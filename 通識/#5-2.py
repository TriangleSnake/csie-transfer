#5-2
a=eval(input("請輸入a的值:"))
b=eval(input("請輸入b的值:"))
c=eval(input("請輸入c的值:"))
if a>b and a>c:
    print(100)
elif c>b and c>a:
    print(10)
elif b>a and b>c:
    print(1)
else:
    print(0)
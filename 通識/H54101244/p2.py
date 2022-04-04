#p2
while 1:
    n=eval(input("輸入整數n:"))
    if n<0:
        print("結束程式")
        break
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end='')
        for j in range(i):
            print("OX",end='')
        print("O")

            
        
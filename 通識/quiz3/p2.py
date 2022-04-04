#p2
a=eval(input("請輸入第 1 個數字:"))
b=eval(input("請輸入第 2 個數字:"))
for i in range(2,min(a,b)+1):
    if a%i==0 and b%i==0:
        print("沒互質!")
        exit()
print("互質!")

    
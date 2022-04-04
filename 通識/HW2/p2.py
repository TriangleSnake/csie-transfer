#p2
a=eval(input("請輸入大於等於1的整數a:"))
if a<1:
    print("錯誤,請輸入大於等於1的整數")
else:
    sum=0
    for i in range(a+1):
        sum+=i
    print("計算結果:",sum)
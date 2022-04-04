#5-3
money=eval(input("請輸入今天賣豆花賺多少錢"))
if (money//100)!=0:
    print(money//100,"個百元")
if (money//10)!=0:
    print(money//100,"個十元")
print(money,"個一元")
a=eval(input("輸入一個整數,範圍1~1000:"))
if a%2==0 and a%3==0:
    print("a是2和3的倍數")
elif a%2==0:
    print("a是2的倍數")
elif a%3==0:
    print("a是3的倍數")
else:
    print("不符以上條件")
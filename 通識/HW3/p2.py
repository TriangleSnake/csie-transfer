#p2
year=eval(input("輸入西元年 = "))
if year%4!=0:
    print("平年")
elif year%100!=0:
    print("閏年")
elif year%400!=0:
    print("平年")
else :
    print("閏年")

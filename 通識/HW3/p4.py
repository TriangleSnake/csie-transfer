#p4
n=eval(input("請輸入天數:"))
days=[10,10,10]
sum=0
print("10 10 10 ",end='')
for i in range(n-3):
    sum=0
    for j in days:
        sum+=j
    days[0]=days[1]
    days[1]=days[2]
    days[2]=sum
    print(days[2],end=' ')
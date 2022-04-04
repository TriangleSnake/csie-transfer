#p4
n=eval(input("輸入n:"))
before=[0,1]
print("0 1 ",end='')
for i in range(n-2):
    now=(before[0]+before[1])*2
    before[0]=before[1]
    before[1]=now
    print(now,end=' ')

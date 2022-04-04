#64-e
x=[]
y=[]
sum=0
for i in range(1,8,2):
    x.append(i)
for i in range(1,11,3):
    y.append(i)
for i in range(4):
    sum+=y[i]**x[i]*(-1)
print(sum)
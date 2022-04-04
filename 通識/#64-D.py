#64-D
sum=0
x=[]
y=[]
for i in range(1,14,3):
    x.append(i)
for i in range(5,18,3):
    y.append(i)
for i in range(5):
    sum+=x[i]*y[i]
print(sum)
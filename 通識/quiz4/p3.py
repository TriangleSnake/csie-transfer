#p3
import random
import re


possible=[]
def comp(tmpa,tmpb):
    tA=0
    tB=0
    for i in range(4):
        for j in range(4):
            if tmpa[i]==tmpb[j]:
                if i==j:
                    tA+=1
                else :
                    tB+=1
    return [tA,tB]
def same(tmp):
    rettmp=0
    for i in range(4):
        for j in range(i+1,4):
            if tmp[i]==tmp[j]:
                rettmp+=1    
    return rettmp
for i in range(111,999):
    tmp='0'+str(i)
    if same(tmp)==0:
        possible.append(tmp)
for i in range(1000,9999+1):
    tmp=str(i)
    if same(tmp)==0:
        possible.append(tmp)
ans=random.choice(possible)
print("答案 =",ans)
while 1:
    guess=input("猜一數字 = ")
    print("結果 =",comp(guess,ans)[0],"x",comp(guess,ans)[1],'y')
    if comp(guess,ans)[0]==4:
        print("答對了")
        break
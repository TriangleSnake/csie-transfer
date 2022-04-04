import random
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
start=True
while 1:
            npossible=[]
            status = [[0 for _ in range(5)] for _ in range(5)]
            min=99999
            for i in possible:
                    mx=0
                    for j in possible:
                        tcmp=comp(i,j)
                        status[tcmp[0]][tcmp[1]]+=1
                    mxls=[]
                    for j in status:
                        mxls.append(max(j))
                    mx=max(mxls)
                    status = [[0 for _ in range(5)] for _ in range(5)]
                    if min>mx:
                        min=mx
                        mnNode=i
                        if start==True:
                                break
            guess=mnNode
            start=False
            print('\n'+guess)
            while 1:
                print("幾A幾B")
                A=input().split()
                B=int(A[1])
                A=int(A[0])
                if (A<=4 and A>=0 and B<=4 and B>=0) :
                    break
                else :
                    print("蛤")
            for i in possible:
                if comp(i,guess)==[A,B]:
                    npossible.append(i)
            if len(npossible)==1:
                print("Answer is:"+str(npossible[0]))
                break
            if npossible==[]:
                print("出事了!你的線索矛盾")
                break
            possible=npossible.copy()
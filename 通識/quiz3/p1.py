#p1
even=0
odd=0
for i in range(10):
    string="第 "+str(i+1)+" 個數字:"
    num=eval(input(string))
    if num%2==0:
        even+=1
    elif num%2==1:
        odd+=1
print("偶數:",even,"個",", 奇數:",odd,"個")

#105-a
score=[]

for i in range(5):
    tmp=[]
    string="請輸入第"+str(i+1)+"位同學國文成績:"
    tmp.append(eval(input(string)))
    string="請輸入第"+str(i+1)+"位同學英文成績:"
    tmp.append(eval(input(string)))
    score.append(tmp)
max=0
fail=0
for i in score:
    if i[0]>max:
        max=i[0]
    if i[1]<60:
        fail+=1
print("國文最高分:",max)
print("英文不及格人數:",fail)

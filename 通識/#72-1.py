#72-1
min=999
max=0
fail=0
for i in range(10):
    string="請輸入第"+str(i+1)+"位同學的成績:"
    tmp=eval(input(string))
    if tmp<min:
        min=tmp
    if tmp>max:
        max=tmp
    if tmp<60:
        fail+=1
print("最高分:",max)
print("最低分:",min)
print("不及格人數:",fail)

#88-2
max=0
fail=0
for i in range(10):
    while 1:
        string="請輸入第"+str(i+1)+"位同學成績:"
        score=eval(input(string))
        if score>100 or score<0:
            print("不合理，請重新輸入")
        else :
            break
    if score>max:
        max=score
    if score<60:
        fail+=1
print("最高分為:",max)
print("不及格人數:",fail)

#105-a
chi=[]
eng=[]
for i in range(5):
    string="請輸入第"+str(i+1)+"位同學國文成績:"
    chi.append(eval(input(string)))
    string="請輸入第"+str(i+1)+"位同學英文成績:"
    eng.append(eval(input(string)))
print("國文最高分:",max(chi))
fail=0
for i in eng:
    if i<60:
        fail+=1
print("英文不及格人數:",fail)

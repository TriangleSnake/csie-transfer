#p2
sum=0
string=''
for i in range(6):
    string='請輸入第'+str(i+1)+'個數字:'
    sum+=eval(input(string))
print("總和:",sum)
print("平均",(sum/6))
#score_inp
sum=0
for i in range(5):
    string="請輸入第"+str(i+1)+"位同學成績:"
    score=eval(input(string))
    sum+=score
print("全總分為:",sum)
aver=sum/5
print("全班平均為:",aver)
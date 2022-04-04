#TOEIC_inp
score=[]
sum=0
for i in range(3):
    string="第"+str(i+1)+"次成績:"
    score.append(eval(input(string)))
    sum+=score[i]
aver=sum/3
print("平均為:",aver)
print("第一次考試與平均差:",aver-score[0])
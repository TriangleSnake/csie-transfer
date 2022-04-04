#TOEIC
score=[700,800,850]
sum=0
for i in score:
    sum+=i
aver=sum/3
print("平均為:",aver)
print("第三次高於平均",(aver-score[2]))
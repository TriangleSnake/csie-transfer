#quiz
from telnetlib import BM


height=eval(input("輸入身高(cm):"))
weight=eval(input("輸入體重(kg):"))
height=height/100
BMI=weight/(height**2)
print("BMI=",BMI)
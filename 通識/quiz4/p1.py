#p1
num=eval(input("輸入一個數:"))
guess=0
while 1:
    if guess*guess>num:
        if num-(guess-1)*(guess-1)<guess**2-num:
            print(guess-1)
        else :
            print(guess)
        break
    guess+=1
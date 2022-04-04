#3-3
temp=eval(input("請輸入溫度:"))
aqi=eval(input("請輸入AQI:"))
if temp>37 or aqi>150:
    print("避免外出")
else :
    print("可依需要待在戶外")

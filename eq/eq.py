try:
    f=open('setting.txt','r',encoding="UTF-8")
    area=f.readline().split('=')[1]
    region=f.readline().split('=')[1]
except:
    print("設定檔有誤")
    exit()

import telepot
import sys
import requests
import datetime
import time
bot=telepot.Bot('1908290137:AAFmO6RjCX6XlrRhyIVl-NTKrsZLkCP1QcQ')
starttime = datetime.datetime.now()
print(starttime)
try:
    message="即將發送測試訊息"
    if sys.argv[1]=='test':
        message='即將發送測試訊息'
    else :
        message=region+'地區地震警報:'+sys.argv[1]+'級地震 將於 '+sys.argv[2]+' 秒後抵達'
except:
    pass
area='tn'
bot.sendMessage('-592407536',message)
url='https://script.google.com/macros/s/AKfycbws1z7qKfn834vOqQWKi5Z31U7zrwyQo42BsEScE9doYia15SlHIf82aH5v8QdeZQYS/exec?token=ss123'+area
r=requests.get(url)
recieve=r.text

if recieve=='-1':
    print("...訊息已由其他電腦發送...")
    exit()

recieve=recieve.split(',')
recieve.pop()
for i in recieve:
    print ('發送至:'+str(i))
    bot.sendMessage(i,message)
    print ('發送成功!')
endtime=datetime.datetime.now()
print(endtime)

while 1:
    if int((endtime-starttime).seconds)>=int(sys.argv[2]):
        break
    else :
        time.sleep(int(sys.argv[2])-int((endtime-starttime).seconds))
        break

print('抵達')
for i in range(3):
    bot.sendMessage('-592407536','抵達')
for i in recieve:
    for j in range(3):
        bot.sendMessage(i,'抵達')
url='https://script.google.com/macros/s/AKfycbws1z7qKfn834vOqQWKi5Z31U7zrwyQo42BsEScE9doYia15SlHIf82aH5v8QdeZQYS/exec?token=ss123end'+area
ret=requests.get(url).text
print("伺服器復位訊息:",ret)
import os
import json
print("等待地震報告中..")
for i in range(480):
    print("\r"+str(480-i)+"秒後取得地震報告",end='')
    time.sleep(1)
url='https://script.google.com/macros/s/AKfycbws1z7qKfn834vOqQWKi5Z31U7zrwyQo42BsEScE9doYia15SlHIf82aH5v8QdeZQYS/exec?token=ss123rep'
if requests.get(url).text=='-1':
    print("---地震報告已由其他電腦接手---")
    exit()

url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-3F8D970F-C6A9-4090-870F-E8492DD6C97A&format=JSON&areaName=%E8%87%BA%E5%8D%97%E5%B8%82'
r=requests.get(url).text
r=json.loads(r)

print(r)
src=r['records']['earthquake'][0]['reportImageURI']
bot.sendPhoto('-592407536',src)
for i in recieve:
    bot.sendPhoto(i,src)

message='詳細地震報告:\n'+r['records']['earthquake'][0]['web']
bot.sendMessage('-592407536',message)
for i in recieve:
    print ('地震報告發送至:'+str(i))
    bot.sendMessage(i,message)
    print ('發送成功!')
url='https://script.google.com/macros/s/AKfycbws1z7qKfn834vOqQWKi5Z31U7zrwyQo42BsEScE9doYia15SlHIf82aH5v8QdeZQYS/exec?token=ss123repend'
ret=requests.get(url).text
print("伺服器復位訊息:",ret)
print('\n')
os.system('taskkill /f /im chromedriver.exe')
print('--地震預警訊息發送完畢--')
os.system('pause')
#update.py
# -*- coding: UTF-8 -*-
import os
from tkinter import W
import requests
import threading

print("正在更新pip")
os.system("python.exe -m pip install --upgrade pip")
print("正在更新python package")
os.system("pip install --upgrade -r requirement.txt")
print("正在更新eq.py")
f=open("eq.py","w",encoding="utf-8")
url="https://raw.githubusercontent.com/TriangleSnake/csie-transfer/main/eq/eq.py"
rewrite=requests.get(url).text
print(rewrite)
f.write(rewrite)
f.close()
print("更新完成")
os.system("pause")
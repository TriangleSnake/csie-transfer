from tkinter.messagebox import showinfo
import cv2
import numpy as np
import os
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import time
import win32gui
import win32con
from selenium.webdriver.common.keys import Keys
from ctypes import windll
os.system('start StartChrome.cmd')
url='https://course.ncku.edu.tw/index.php?c=auth'
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get(url)

def wait(ele):
    while 1:
        try:
            return driver.find_element(By.CLASS_NAME,ele)
        except:
            print('\rwaiting',end='')
while 1:
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    ele=wait('click')
    ActionChains(driver).move_to_element(ele).context_click(ele).perform()
    pyautogui.hotkey('shift')
    time.sleep(1)
    pyautogui.typewrite('y')
    if ImageGrab.grabclipboard()!=None:
        img=np.array(ImageGrab.grabclipboard())
        img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        cv2.imshow('img',img)
        hwnd = win32gui.FindWindow(None,'img')
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
        per_num=[]
        for i in range(4):   
            per_num.append(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)[0:20,9+i*9:19+i*9])
        opt=''
        for k in range(len(per_num)):
            for i in range(len(per_num[k])):#i=y
                for j in range(len(per_num[k][0])-1):#j=x
                    if per_num[k][i][j]<30:
                        per_num[k][i][j]=0
                        img[i][9+j+k*9]=[255,0,0]
                    else :
                        per_num[k][i][j]=255
                        img[i][9+j+k*9]=[255,255,255]
                    per_num[k][i][len(per_num[k][0])-1]=255
                cv2.imshow('img',cv2.resize(img,(len(img[0])*10,len(img)*10)))
                cv2.waitKey(10)

            min=25500
            for l in range(10):
                tmp=0
                string=str(l)+'.png'
                tmpimg=cv2.imread(string)
                tmpimg=cv2.cvtColor(tmpimg,cv2.COLOR_BGR2GRAY)
                showimg=cv2.add(per_num[k],tmpimg, dst=None, mask=None)
                tmpimg=cv2.bitwise_xor(per_num[k],tmpimg, dst=None, mask=None)
                for i in tmpimg:
                    for j in i:
                        tmp+=j
                if tmp<min:
                    min=tmp
                    mnNum=str(l)
                    for i in range(len(per_num[k])):#i=y
                        for j in range(len(per_num[k][0])-1):
                            if showimg[i][j]>150:
                                img[i][9+j+k*9]=[255,255,255]
                            else :
                                img[i][9+j+k*9]=[0,0,255]
                        cv2.imshow('img',cv2.resize(img,(len(img[0])*10,len(img)*10)))
                        cv2.waitKey(1)
            opt+=mnNum
            ele=driver.find_element(By.ID,'code')
            ele.send_keys(mnNum)
            for i in range(len(per_num[k])):#i=y
                        for j in range(len(per_num[k][0])-1):
                            if np.allclose(img[i][9+j+k*9],[0,0,255]):
                                img[i][9+j+k*9]=[0,255,0]
            
            cv2.imshow('img',cv2.resize(img,(len(img[0])*10,len(img)*10)))
            cv2.waitKey(30)
        ele=driver.find_element(By.ID,'code')
        
        ele.send_keys(Keys.ENTER)
        #driver.refresh()
        print(opt)
    cv2.waitKey(30)

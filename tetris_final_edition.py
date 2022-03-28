#tetris
from numpy.core.fromnumeric import put
from numpy.core.shape_base import block
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import ImageGrab
import cv2
import numpy
import time
import os
import win32con
import win32gui
import pyautogui
import copy

x=[]
y=[]
for i in range(20):
    y.append(16+i*33)
for i in range(10):
    x.append(16+i*32)

img=ImageGrab.grab()
img=cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
img=img[174:900,800:1120]
cv2.imshow('a',img)
hwnd = win32gui.FindWindow(None, "a")
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
def putmoudle(status):
    match status:
        case [0,0,1,1,1,1]:
            cv2.putText(img,'Orangerick',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 1
        case [0,1,0,1,1,1]:
            cv2.putText(img,'Teewee',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 2
        case [0,1,1,1,1, 0]:
            cv2.putText(img,'RhodeislandZ',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 3
        case [0,1,1,0,1,1]:
            cv2.putText(img,'Smashboy',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 4
        case [1,0,0,1,1,1]:
            cv2.putText(img,'Bluerick',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 5
        case [1,1,0,0,1,1]:
            cv2.putText(img,'ClevelandZ',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 6
        case [0,0,0,1,1,1]:
            cv2.putText(img,'Hero',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 7
        case _:
            cv2.putText(img,'None',(x[6],y[0]),0,0.7,(255,0,0),2)
            return 0
            
def fndhol(anal):
    sum=0
    sub=0
    for i in range(10):
        for j in range(20):
            if anal[j][i]==0:
                sum+=1
    for i in range(10):
        for j in range(20):
            if anal[j][i]==0:
                sub+=1
            else :
                break
    return sum-sub
def fndtop(anal):
    sub=0
    for j in range(20):
        btl=True
        for i in range(10):
            if anal[19-j][i]==1:
                btl=False
                break
        if btl==True:
            return j
    return 99   
def fndupblock(anal):
    ret=0
    for i in range(20):
        for j in range(10):
            if anal[i][j]==0:
                ret+=i
    return ret/200
def fnd(n,m,anal,r):
        mmin=99999
        for i in range(10):
            for j in range(20):
                if (anal[j+m[0]+1][i+n[0]]!=0 or anal[j+m[1]+1][i+n[1]]!=0 or anal[j+m[2]+1][i+n[2]]!=0 or anal[j+m[3]+1][i+n[3]])!=0:
                    anal[j+m[0]][i+n[0]]=1
                    anal[j+m[1]][i+n[1]]=1
                    anal[j+m[2]][i+n[2]]=1
                    anal[j+m[3]][i+n[3]]=1
                    ckremove=copy.deepcopy(anal)
                    clear=0
                    for k in range(20):
                        full=True
                        for l in range(10):
                            if ckremove[k][l]==0:
                                full=False
                        if full==True:
                            clear+=1
                            for l in range(k):
                                ckremove[k-l]=ckremove[k-l-1]
                            for l in range(20-fndtop(ckremove)):
                                ckremove[l]=[0,0,0,0,0,0,0,0,0,0,1,1,1]
                    
                    tp=fndhol(ckremove)*(100)+fndtop(ckremove)*10+fndupblock(ckremove)*3
                    if tp<mmin:
                        mmin=tp
                        po=i
                        tpanal=copy.deepcopy(ckremove)
                    anal[j+m[0]][i+n[0]]=0
                    anal[j+m[1]][i+n[1]]=0
                    anal[j+m[2]][i+n[2]]=0
                    anal[j+m[3]][i+n[3]]=0
                    break
        return [mmin,po,r,tpanal]


column,row=21,13
hasblock=[[1]*row for _ in range(column)]
for i in range(20):
    for j in range(10):
        hasblock[i][j]=0

while 1:
    min=[9999999,0,0,copy.deepcopy(hasblock)]
    img=ImageGrab.grab()
    img=cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    det=img.copy()
    det=cv2.cvtColor(numpy.array(det),cv2.COLOR_RGB2GRAY)
    det=det[177:243,896:992]
    
    img=img[240:900,800:1120]
    gray=img.copy()
    gray=cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
    ham=[]

    for i in range(2):#偵測方塊種類
        for j in range(3):
            if det[14+i*33][16+j*32]>65:
                cv2.rectangle(det,(16+j*32,14+i*33),(16+j*32,14+i*33),(255,255,255),3)
                ham.append(1)
            else :
                ham.append(0)
                cv2.rectangle(det,(16+j*32,14+i*33),(16+j*32,14+i*33),(0,0,0),3)
    
    for i in range(10):#畫面更新
        for j in range(20):
            if hasblock[j][i] ==0:
                cv2.rectangle(img,(x[i],y[j]),(x[i],y[j]),(0,255,0),3)
                cv2.putText(img,str(gray[y[j]][x[i]]),(x[i]-16,y[j]-16),0,0.3,(0,255,0),1)
            else :
                cv2.rectangle(img,(x[i],y[j]),(x[i],y[j]),(0,0,255),3)
                cv2.putText(img,str(gray[y[j]][x[i]]),(x[i]-16,y[j]-16),0,0.3,(0,0,255),1)
    cv2.imshow('b',det)
    hwnd = win32gui.FindWindow(None, "b")
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)

    cv2.putText(img,"top:"+str(fndtop(hasblock)),(0,600),0,1,(0,0,255),2)
    cv2.putText(img,"hol"+str(fndhol(hasblock)),(0,650),0,1,(0,0,255),2)

    status=putmoudle(ham)
    tmp=0
    pos=0
    rot=0
    if status>0:
        match status:
                    case 1:
                        n=[2,0,1,2]
                        m=[0,1,1,1]
                        r=0
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,0,0,1]
                        m=[0,1,2,2]
                        r=1
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,1,2,0]
                        m=[0,0,0,1]
                        r=2
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,1,1,1]
                        m=[0,0,1,2]
                        r=3
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                    case 2:
                        n=[1,0,1,2]
                        m=[0,1,1,1]
                        r=0
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,0,1,0]
                        m=[0,1,1,2]
                        r=1
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,1,2,1]
                        m=[0,0,0,1]
                        r=2
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[1,0,1,1]
                        m=[0,1,1,2]
                        r=3
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)

                    case 3:
                        n=[1,2,0,1]
                        m=[0,0,1,1]
                        r=0
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,0,1,1]
                        m=[0,1,1,2]
                        r=1
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                    
                    case 4:
                        n=[0,1,0,1]
                        m=[0,0,1,1]
                        r=0
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)

                    case 5:
                        n=[0,0,1,2]
                        m=[0,1,1,1]
                        r=0
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)

                        n=[0,1,0,0]
                        m=[0,0,1,2]
                        r=1
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,1,2,2]
                        m=[0,0,0,1]
                        r=2
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[1,1,0,1]
                        m=[0,1,2,2]
                        r=3
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)

                    case 6:
                        n=[0,1,1,2]
                        m=[0,0,1,1]
                        r=0
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)

                        n=[1,0,1,0 ]
                        m=[0,1,1,2]
                        r=1
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)

                    case 7:
                        
                        
                        n=[0,1,2,3]
                        m=[0,0,0,0]
                        r=0
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m,tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
                        n=[0,0,0,0]
                        m=[0,1,2,3]
                        r=1
                        tmphasblock=copy.deepcopy(hasblock)
                        tmp=fnd(n,m, tmphasblock,r)
                        if min[0]>tmp[0]:
                            min=copy.deepcopy(tmp)
        
        pos=min[1]
        rot=min[2]
        pyautogui.PAUSE=0.03
        
        for i in range(rot):
            pyautogui.press ('up')
        pyautogui.sleep(0.03)
        if rot==1 or status==4:
            if status==7:
                if pos>5:
                    pos-=5
                    for i in range(pos):
                        pyautogui.press('right')
                else:
                    pos=5-pos
                    for i in range(pos):
                        pyautogui.press('left')
            else:
                if pos>4:
                    pos-=4
                    for i in range(pos):
                        pyautogui.press('right')
                else :
                    pos=4-pos
                    for i in range(pos):
                        pyautogui.press('left')
        else:
            if pos>3:
                pos-=3
                for i in range(pos):
                    pyautogui.press('right')
            else:
                pos=3-pos
                for i in range(pos):
                    pyautogui.press('left')
        pyautogui.sleep(0.03)
        pyautogui.press('space')
        pyautogui.sleep(0.03)
        
    cv2.putText(img,str(min),(0,500),0,1,(0,0,255),1)
    cv2.imshow('a' ,img)
    cv2.waitKey(1)
    hasblock=copy.deepcopy(min[3])
    
    status=0

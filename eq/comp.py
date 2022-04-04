import time
import cv2





def scan(imga,imgb,option=0):
    
    fpa=[]
    fpb=[]
    imga=cv2.resize(imga,(450,450))
    imgb=cv2.resize(imgb,(450,450))
    if option==1:
        imga = imga[66:384,66:384]
        imgb = imgb[66:384,66:384]
    imgaRES=cv2.resize(imga,(9,8))
    imgbRES=cv2.resize(imgb,(9,8))
    imgaRES=cv2.cvtColor(imgaRES, cv2.COLOR_BGR2GRAY)
    imgbRES=cv2.cvtColor(imgbRES, cv2.COLOR_BGR2GRAY)
    for i in range(8):
        for j in range(8):
            if imgaRES[i][j]>imgaRES[i][j+1]:
                fpa.append(1)
            else :
                fpa.append(0)
            if imgbRES[i][j]>imgbRES[i][j+1]:
                fpb.append(1)
            else :
                fpb.append(0)

    point = [[1],[2]]
    imga=cv2.resize(imga,(450,450))
    imgb=cv2.resize(imgb,(450,450))
    for i in range(len(fpa)):
        x=(i%8)*50+25
        y=int(i/8)*50+25
        if fpa[i]==fpb[i]:
            imga=cv2.rectangle(imga,(x,y),(x+45,y+45),(0,255,0))
            imgb=cv2.rectangle(imgb,(x,y),(x+45,y+45),(0,255,0))
            cv2.imshow('a',imga)
            cv2.imshow('b',imgb)
            cv2.waitKey(5)
            #cv2.destroyAllWindows()
        else:
            imga=cv2.rectangle(imga,(x,y),(x+45,y+45),(0,0,255))
            imgb=cv2.rectangle(imgb,(x,y),(x+45,y+45),(0,0,255))
            cv2.imshow('a',imga)
            cv2.imshow('b',imgb)
            cv2.waitKey(1)
            #cv2.destroyAllWindows()

    print (fpa)
    print (fpb) 
    k=0
    for i in range(len(fpa)):
        if fpa[i]==fpb[i]:
            k=k+1
        

    k=(k/0.64)
    return k


if __name__=='__main__':
    img1=cv2.imread('a.jpg')
    img2=cv2.imread('b.jpg')
    print(scan(img1,img2,1))
    cv2.waitKey(0)
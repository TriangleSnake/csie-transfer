from comp import scan
from bs4 import BeautifulSoup as Soup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from skimage import io
import cv2
import parser
import numpy
from lxml import etree

imga=cv2.imread('test.jpg')

from selenium.webdriver.chrome.options import Options
  
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)

username=''
pwd=''


def login():
    url='https://www.instagram.com/'

    driver.get(url)
    while 1:
        try :
            driver.find_element_by_name("username")
            break
        except:
            pass
    element = driver.find_element_by_name("username")
    element.click()
    element.send_keys(username)
    element =driver.find_element_by_name("password")
    element.click()
    element.send_keys(pwd)
    element = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')                        #login botton
    element.click()
    wait('//*[@id="react-root"]/section/main/div/div/div/div/button')
    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    element.click()                                                                                         #save file button

def wait(ele):
    while 1:
        try :
            driver.find_element_by_xpath(ele)
            break
        except:
            pass


url = "https://www.instagram.com/trianglesnake/"                                                        #profile
driver.get(url)
wait('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')                                    #follower





sum=Soup(driver.page_source,'html.parser')                                                                 #gross followers number
sum =sum.find('a').span.get('title')
sum=int(sum)
print(sum)


element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')

element.click()
wait('/html/body/div[6]/div/div/div[2]/ul/div/li[2]')
while 1 :
    flag=0
    imgscr=Soup(driver.page_source,'html.parser')
    imgscr=imgscr.find('div',{'class':'isgrP'})
    if type(imgscr)!='NoneType':
        imgscr=imgscr.find_all('img')
        if imgscr!=[]:
            flag=1
    if flag==1:
        break
    




for i in range(406):
    print ('start')
    imgscr=Soup(driver.page_source,'html.parser')
    imgscr=imgscr.find('div',{'class':'isgrP'})
    imgscr=imgscr.find_all('img')
    for j in range(len(imgscr)):
        imgscr[j]=imgscr[j].get('src')
    image = io.imread(imgscr[i],format='JPEG')
    driver.execute_script('document.querySelector("body > div.RnEpo.Yx5HN > div > div > div.isgrP").scrollTo(0,document.querySelector("body > div.RnEpo.Yx5HN > div > div > div.isgrP").scrollHeight)')
    for k in range(len(image)):
        for j in range(len(image[k])):
            tmp=image[k][j][0]
            image[k][j][0]=image[k][j][2]
            image[k][j][2]=tmp



    result=scan(image,imga) #0 no frame 1 with frame



    print (str(result)+'%')
    if result>=80:
        print (str(result)+'%MATCH!')
        result=i+1
        cv2.waitKey(0)
        break
    print ('end')   
element=driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li['+str(result)+']/div/div[1]/div[2]/div[1]/span/a')
element.click()
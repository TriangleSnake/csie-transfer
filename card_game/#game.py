#game
from cProfile import label
from PIL import ImageTk,Image
import pyautogui
import time
import tkinter as tk
window=tk.Tk()
window.configure(bg='black')
window.attributes('-fullscreen',True)
canvas=tk.Canvas(width=1920,height=1050)
card_width=1850//13
card_height=1024//55

img=[]
for i in range(1,14):
    img_pil=Image.open('p'+str(i)+'.png')
    img.append(ImageTk.PhotoImage(img_pil))
for i in range(1,14):
    canvas.create_image(10+i*(card_width-20),800,image=img[i-1],anchor='nw',tags='p'+str(i))
    canvas.pack()
text=tk.Entry(window,width=100,justify="center")
window.update()
while 1:
    mouse_x, mouse_y= pyautogui.position()
    loc=(mouse_x-10)//(card_width-20)
    canvas.bind("<Button>",lambda x:canvas.delete(['p'+str(loc)]))
    text.delete(0,tk.END)
    text.insert(0,str(mouse_x)+","+str(mouse_y)+","+str(loc))
    text.pack()
    window.update()
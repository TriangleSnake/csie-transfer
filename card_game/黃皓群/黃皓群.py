import tkinter as tk
from PIL import Image, ImageTk
import random
screen_w=1920
screen_h=1000
card_w=76
card_h=115
root=tk.Tk()
root.geometry(str(screen_w)+"x"+str(screen_h))
root.state('zoomed')
fold_img=[]
fold=[]
index=0
add_entry=''
add_text=''
player=-1
add_money=0
add_entry=tk.Entry(root,bd=5)
bt_send=''
bt_next=''
def add_m():
    global add_money,money,bt_next,money
    try:
        print(add_entry.get())
        eval(add_entry.get())
    except:
        add_text.configure(text="請輸入數字")
        return 0
    if eval(add_entry.get())>money[player]:
        add_text.configure(text="不得超過總籌碼")
    elif eval(add_entry.get())<=0:
        add_text.configure(text="不得為0或負數")
    else:
        add_money+=eval(add_entry.get())
        money[player]-=add_money
        add_text.configure(text='成功下注'+add_entry.get())
        text_money.configure(text="總籌碼"+str(money[player]))
        bt_next=tk.Button(root,text="NEXT",bg='green',command=round)
        bt_send.place_forget()
        bt_next.place(x=screen_w*3//4+150,y=screen_h*3//4+20)
def show(event=0):
    global player,card_img
    fold[5].configure(image=card_img[player*13])
    fold[6].configure(image=card_img[player*13+1])
    

def round():
    global add_text,add_entry,player,bt_send
    try:
        bt_next.place_forget()
    except:
        pass
    fold[5].configure(image=fold_img[5])
    fold[6].configure(image=fold_img[6])
    player+=1
    player%=4
    start_button.place_forget()
    text_money.configure(text="籌碼:"+str(money[player]))
    text_money.place(x=screen_w*3//4,y=screen_h//4)
    fold[5].bind("<Button-1>",show)
    fold[6].bind("<Button-1>",show)
    add_text=tk.Label(root,text="下注")
    add_text.place(x=screen_w*3//4,y=screen_h*3//4)   
    add_entry=tk.Entry(root,bd=5)
    add_entry.place(x=screen_w*3//4,y=screen_h*3//4+20)
    bt_send=tk.Button(root,text='send',bg='red',command=add_m)
    bt_send.place(x=screen_w*3//4+150,y=screen_h*3//4+20)

    
card=[]
for i in 'cdhs':
    for j in range(1,14):
        card.append(i+str(j))

random.shuffle(card)


for i in range(5):
    fold_img.append(tk.PhotoImage(file='fold.png'))
    fold.append(tk.Label(root,image=fold_img[i],anchor='nw'))
    fold[i].place(x=screen_w/2-int(2.5*card_w)+card_w*i,y=screen_h/2-card_h//2)
    index+=1
for i in range(2):#玩家的排index5~6
    fold_img.append(tk.PhotoImage(file='fold.png'))
    fold.append(tk.Label(root,image=fold_img[index],anchor='nw'))
    fold[index].place(x=screen_w/2-card_w+card_w*i,y=screen_h-card_h)
    index+=1
for i in range(2):
    fold_img.append(tk.PhotoImage(file='fold.png'))
    fold.append(tk.Label(root,image=fold_img[index],anchor='nw'))
    fold[index].place(x=screen_w/2-card_w+card_w*i,y=0)
    index+=1
for i in range(2):
    tmp_img=Image.open('fold_r.png')
    fold_img.append(ImageTk.PhotoImage(tmp_img))
    fold.append(tk.Label(root,image=fold_img[index],anchor='nw'))
    fold[index].place(x=0,y=screen_h/2-card_w+i*card_w)
    index+=1
for i in range(2):
    tmp_img=Image.open('fold_r.png')
    fold_img.append(ImageTk.PhotoImage(tmp_img))
    fold.append(tk.Label(root,image=fold_img[index],anchor='nw'))
    fold[index].place(x=screen_w-card_h,y=screen_h/2-card_w+i*card_w)
    index+=1
money=[]
for i in range(4):
    money.append(10000)
start_button=tk.Button(root,bg='red',text="START",command=round)
start_button.place(x=screen_w*4//5,y=screen_h*4//5)
text_money=tk.Label(root)
card_img=[]
for i in range(52):
    card_img.append((tk.PhotoImage(file=card[i]+'.png')))
root.mainloop()
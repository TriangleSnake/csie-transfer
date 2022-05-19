# card_game2.0
from concurrent.futures import thread
import pyautogui
from PIL import Image, ImageTk
import random
import tkinter as tk
import time
import threading
import requests
url = "https://script.google.com/macros/s/AKfycbzFEz320cCllRmd63A4NsZbMBTdWFpQ_Xw5euIYaF_1vDRSwCmB6VGBdWdRAg1Uep2gEQ/exec"


def hidemenu():
    hidelst = [bt_option, bt_start, bt_quit, bt_back, text_option,
               text_name, entry_name, text_room_name, entry_room_name, bt_join_room]
    for i in hidelst:
        i.pack_forget()


def start():
    hidemenu()
    text_name.pack()
    entry_name.pack()
    text_room_name.pack()
    entry_room_name.pack()
    bt_join_room.pack()
    bt_back.pack()
    entry_name.insert(0, "123")
    entry_room_name.insert(0, "123")


def option():
    hidemenu()
    text_option.pack()
    bt_back.pack()

 

def menu():
    hidemenu()
    title_menu.pack(side='top')
    div_menu.pack()
    bt_start.pack()
    bt_option.pack()
    bt_quit.pack()
    title_menu.pack()


def errormsg(msg):
    text_console.delete(0, tk.END)
    text_console.insert(0, msg)
    text_console.pack()


def join_room():
    global room_name, name
    name = entry_name.get()
    room_name = entry_room_name.get()

    if name == '':
        errormsg("please enter a name!")
        start()
    elif room_name == '':
        errormsg("please enter room name!")
        start()
    else:
        start_game()


def send():
    global choosed,card
    requests.get(url+"?send=1&room="+room_name+"&name="+name+"&card="+str(choosed))
    requests.get(url+"?room="+room_name+"&name="+name+"&card_num="+str(len(card)))

    for i in choosed:
        card.remove(i)
    choosed=[]
    if card==[]:
        requests.get(url+"&room="+room_name+"&name="+name+"&win=1")
        game_over(1)
    bt_pass.configure(state="normal",bg="green")
    show_card(card)

def game_over(self=0):
    if self==0:
        pass
    else :
        pass


choosed = []


def choose(card, lst, loc):
    global choosed,current_card
    
    if card in choosed:
        canvas.delete(lst[loc])
        canvas.create_image(10+loc*(card_width-20), screen_height*7//10,
                            image=img[loc], anchor='nw', tags=lst[loc])
        choosed.remove(card)
    else:
        choosed.append(card)
        canvas.delete(lst[loc])
        canvas.create_image(10+loc*(card_width-20), screen_height*6//10,
                            image=img[loc], anchor='nw', tags=lst[loc])
    if check()==True:
        bt_send.configure(state="normal",bg='green')
    else :
        bt_send.configure(state="disabled",bg='red')
def check():
    ret=False
    global choosed,current_card
    if choosed==[]:
        return ret
    choosed_type=checktype(choosed)
    
    if eval(current_card)==['P'] and choosed_type[0]!=0:
        return True
    elif eval(current_card)==['P'] and choosed_type[0]==0:
        return False
    else:
        current_card_type=checktype(eval(current_card))
    if ('p3' in choosed) and choosed_type[0]!=0:
        return True
    if choosed_type[0]==0:
        return ret
    if choosed_type[0]==current_card_type[0]:
        if eval(choosed_type[1][1:])>eval(current_card_type[1][1:]):
            ret=True
        elif eval(choosed_type[1][1:])==eval(current_card_type[1][1:]) and ord(choosed_type[1][0])>ord(current_card_type[1][0]):
            ret=True
    elif choosed_type[0]==4:
        if current_card_type[0]!=6 and current_card_type[0]!=4:
            ret=True
        elif current_card_type[0]==4 and eval(current_card_type[1][1:])<eval(choosed_type[1][1:]):
            ret=True
    elif choosed_type[0]==6:
        if current_card_type[0]!=6:
            ret=True
        elif eval(current_card_type[1][1:])<eval(choosed_type[1][1:]) or (eval(current_card_type[1][1:])==eval(choosed_type[1][1:]) and ord(current_card_type[1][0])<ord(choosed_type[1][0])):
            ret=True
    return ret

def checktype(lst):
    mx=str(-1)
    lst.sort()
    number=[]
    suit=[]
    ret=0
    for i in lst:
        suit.append(i[0])
        number.append(eval(i[1:]))
    number.sort()
    suit.sort()
    if len(lst)==1:#單張
        ret=1
        mx=lst[0]
    elif len(lst)==2:#pair
        if len(set(number))==1:
            ret=2
            mx=lst[1]
    elif len(lst)==3:#條
        if len(set(number))==1:
            ret=3
            mx=lst[2]
    elif len(lst)==5:
        if len(set(number))==2:
            if number[2]==number[1] and number[2]==number[3]:#鐵支
                ret=4
            else:
                ret=5
            mx=str(number[2])
        elif len(set(number))==5:
            if number[4]==number[0]+4 or number==[1,10,11,12,13]:
                if len(set(suit))==1:
                    ret=6
                else :
                    ret=7
                for i in lst:
                    if str(number[4]) in i:
                        mx=i
    if eval(mx[1:]) <= 2:
        mx=mx[0]+str(eval(mx[1:])+13)
    return ret,mx
def preview(loc, lst):
    global img
    canvas.delete(lst[loc])
    canvas.create_image(10+loc*(card_width-20), screen_height*7//10,
                        image=img[loc], anchor='nw', tags=lst[loc])
img_c=[]

def show_player_status():
    print(123)
    global r
    player_lst=[]
    player_lst.append(r['player1'])
    player_lst.append(r['player2'])
    player_lst.append(r['player3'])
    player_lst.append(r['player4'])
    print(player_lst)
    img1=Image.open('fold.png')
    img1=img1.resize((70,103))
    img1=ImageTk.PhotoImage(img1)
    canhei=1
    canwid=1
    for i in range(len(player_lst)):
        canvas1.create_text(100,0,justify="left",text=player_lst[i]["name"],anchor='nw',tags=player_lst[i]["name"])
        for j in range(eval(player_lst[i]["number"])):
            canvas1.create_image(10,0,image=img1,anchor='nw')
    canvas1.place(x=screen_width*11//13+2,y=0)
    window.update()

def show_current_card(lst):
    show_player_status()
    global img_c
    img_c=[]
    if lst==['P']:
        return 0
    for i in lst:
        img_pil = Image.open(str(i)+'.png')
        img_c.append(ImageTk.PhotoImage(img_pil))
    for i in range(len(img_c)):
        canvas.create_image((screen_width*11//13)/2-(len(img_c)/2-i)*card_width,screen_height*3//10,image=img_c[i],anchor='nw',tags="current_"+lst[i])
    
    

img = []
def Pass():
    global current_card,room_name,name
    requests.get(url+"?send=1&pass=1&room="+room_name+"&name="+name+"&card="+current_card)
current_card=[]
r=''
def refwait():
    global r
    r=eval(requests.get(url+"?name="+name+"&room="+room_name+"&wait=1").text)
    
def show_card(lst):
    global img, choosed,name,room_name,current_card
    requests.get(url+"?room="+room_name+"&name="+name+"&card_num="+str(len(card)))
    global r
    hidemenu()
    img = []
    for i in lst:
        img_pil = Image.open(str(i)+'.png')
        img.append(ImageTk.PhotoImage(img_pil))
    for i in range(len(lst)):
        canvas.create_image(10+i*(card_width-20), screen_height*8//10,
                            image=img[i], anchor='nw', tags=lst[i])
    canvas1.place(x=screen_width*11//13+2,y=0)
    canvas.place(x=0, y=0)
    
    last = 0
    t=int(time.time())
    r=eval(requests.get(url+"?name="+name+"&room="+room_name+"&wait=1").text)
    current_card=r['card']
    show_current_card(eval(current_card))
    show_player_status()
    bt_send.configure(state="disabled",bg='red')
    if eval(current_card)==['P']:
        bt_pass.configure(state="disabled",bg="red")
    while True:
        window.update()
        mouse_x, mouse_y = pyautogui.position()
        loc = (mouse_x-10)//(card_width-20)
        if 0 <= loc < len(lst):
            if lst[loc] not in choosed:
                preview(loc, lst)
            canvas.bind("<Button-1>", lambda x: choose(lst[loc], lst, loc))
        if last != loc and 0 <= loc < len(lst):
            if (lst[last] not in choosed):
                canvas.delete(lst[last])
                canvas.create_image(10+last*(card_width-20), screen_height*8//10,
                                image=img[last], anchor='nw', tags=lst[last])
            last = loc
        if t+1<int(time.time()):
            threading.Thread(target=refwait).start()
            t=int(time.time())
        if current_card!=r['card']:
            for i in eval(current_card):
                canvas.delete(["current_"+i])
            current_card=r['card']
            show_current_card(eval(current_card))
            
        if r['turn']==name:
            bt_send.place(x=screen_width*12//14,y=screen_height*8//10)
            bt_pass.place(x=screen_width*13//14,y=screen_height*8//10)
            text_turn.place_forget()
        else :
            bt_send.place_forget()
            bt_pass.place_forget()
            text_turn.place(x=screen_width*12//14,y=screen_height*8//10)
        window.update()
        
card=[]
def start_game():
    global room_name, name,card
    r = requests.get(url+"?start=1&room="+room_name+"&name="+name).text
    print(r)
    r = eval(r)
    print(r)
    card = []
    if r['is_exist'] == "false":
        errormsg("The room doesn't exist, creating "+room_name)
        for i in 'pqrs':
            for j in range(1, 14):
                card.append(i+str(j))
        random.shuffle(card)
        r = requests.get(url+"?create_room="+room_name +
                 "&name="+name+"&card="+str(card))
        r=eval(r.text)
        card = r['card']
    elif r['is_exist'] == "true":
        errormsg("Joined!")
        card = r['card']
    elif r['is_exist'] == 'full':
        errormsg("The room is full")
        entry_name.delete(0,tk.END)
        entry_room_name.delete(0,tk.END)
        start()
    print(card)
    card = eval(card)
    if 'p3' in card:
        requests.get(url+"?first="+name+"&room="+room_name)
        bt_pass.configure(state="disabled",bg="red")
    show_card(card)


room_name = ''
name = ''


window = tk.Tk()
window.attributes('-fullscreen', True)
window.configure(bg="black")

window.title("大老二")
title_menu = tk.Label(window, text="Deuces2.0",
                      background="white", font=('Arial', 40))
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
div_menu = tk.LabelFrame(window, width=40, height=100,
                         background="black")
menu_button_height = 5
menu_button_width = menu_button_height*10
bt_start = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                     text='START', bg='green', fg='white', command=start)
bt_option = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                      text='OPTION', bg='green', fg='white', command=option)
bt_quit = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                    text='QUIT', bg='green', fg='white', command=quit)

bt_back = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                    text='BACK', bg='green', fg='white', command=menu)

text_name = tk.Label(div_menu, text="Your nickname", bg="black",
                     fg="white", bd=0, font=("Arial", 18))
entry_name = tk.Entry(div_menu, width=menu_button_width, justify="center")

bt_join_room = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                         text='JOIN', bg='green', fg='white', command=join_room)
text_option = tk.Label(div_menu, text="You have no option but to go back", bg="black",
                       fg="white", bd=0, font=("Arial", 18))
text_console = tk.Entry(div_menu, width=menu_button_width, justify="center")
canvas = tk.Canvas(window, width=screen_width, height=screen_height,
                   bg="black", borderwidth=0)
bt_send = tk.Button(window, width=10, height=10,
                    text='SEND', bg='green', fg='white', command=send)
text_room_name = tk.Label(div_menu, text="Room name", bg="black",
                          fg="white", bd=0, font=("Arial", 18))
entry_room_name = tk.Entry(div_menu, width=menu_button_width, justify="center")
canvas = tk.Canvas(width=screen_width*11//13, height=screen_height,
                   bg="black", borderwidth=0)
card_width = 1850//13
bt_pass=tk.Button(window, width=10, height=10,
                    text='PASS', bg='green', fg='white', command=Pass)
text_turn= tk.Label(div_menu, text="It's not your turn", bg="black",
                       fg="white", bd=0, font=("Arial", 18))
bt_send.configure(state="disabled",bg='red')
canvas1=tk.Canvas(window,width=screen_width*2//13,height=screen_height*3//4,bg='black',bd=0)
menu()
window.mainloop()

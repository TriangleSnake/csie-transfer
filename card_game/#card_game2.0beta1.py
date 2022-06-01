# card_game2.0
import pyautogui
from PIL import Image, ImageTk
import random
import tkinter as tk
import time
import threading
import requests
import os
url = "https://script.google.com/macros/s/AKfycbzFEz320cCllRmd63A4NsZbMBTdWFpQ_Xw5euIYaF_1vDRSwCmB6VGBdWdRAg1Uep2gEQ/exec"


def hidemenu():
    pack_hidelst = [bt_option, bt_start, bt_quit, bt_back, text_option,
               text_name, entry_name, text_room_name, entry_room_name, bt_join_room]
    place_hidelst=[canvas, canvas1, bt_send, bt_pass, player1, player2, player3, player4,back,c_1,c_2,c_3,c_4]
    for i in pack_hidelst:
        i.pack_forget()
    for i in place_hidelst:    
        i.place_forget()


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
    global choosed, card
    requests.get(url+"?send=1&room="+room_name +
                 "&name="+name+"&card="+str(choosed))
    requests.get(url+"?room="+room_name+"&name=" +
                 name+"&card_num="+str(len(card)))

    for i in choosed:
        card.remove(i)
    choosed = []
    bt_pass.configure(state="normal", bg="green")
    show_card(card)


choosed = []


def choose(card, lst, loc):
    global choosed, current_card

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
    if check() == True:
        bt_send.configure(state="normal", bg='green')
    else:
        bt_send.configure(state="disabled", bg='red')


def check():
    ret = False
    global choosed, current_card
    if choosed == []:
        return ret
    choosed_type = checktype(choosed)

    if eval(current_card) == ['P'] and choosed_type[0] != 0:
        return True
    elif eval(current_card) == ['P'] and choosed_type[0] == 0:
        return False
    else:
        current_card_type = checktype(eval(current_card))
    if ('p3' in choosed) and choosed_type[0] != 0:
        return True
    if choosed_type[0] == 0:
        return ret
    if choosed_type[0] == current_card_type[0]:
        if eval(choosed_type[1][1:]) > eval(current_card_type[1][1:]):
            ret = True
        elif eval(choosed_type[1][1:]) == eval(current_card_type[1][1:]) and ord(choosed_type[1][0]) > ord(current_card_type[1][0]):
            ret = True
    elif choosed_type[0] == 4:
        if current_card_type[0] != 6 and current_card_type[0] != 4:
            ret = True
        elif current_card_type[0] == 4 and eval(current_card_type[1][1:]) < eval(choosed_type[1][1:]):
            ret = True
    elif choosed_type[0] == 6:
        if current_card_type[0] != 6:
            ret = True
        elif eval(current_card_type[1][1:]) < eval(choosed_type[1][1:]) or (eval(current_card_type[1][1:]) == eval(choosed_type[1][1:]) and ord(current_card_type[1][0]) < ord(choosed_type[1][0])):
            ret = True
    return ret


def checktype(lst):
    mx = str(-1)
    lst.sort()
    number = []
    suit = []
    ret = 0
    for i in lst:
        suit.append(i[0])
        number.append(eval(i[1:]))
    number.sort()
    suit.sort()
    if len(lst) == 1:  # 單張
        ret = 1
        mx = lst[0]
    elif len(lst) == 2:  # pair
        if len(set(number)) == 1:
            ret = 2
            mx = lst[1]
    elif len(lst) == 3:  # 條
        if len(set(number)) == 1:
            ret = 3
            mx = lst[2]
    elif len(lst) == 5:
        if len(set(number)) == 2:
            if number[2] == number[1] and number[2] == number[3]:  # 鐵支
                ret = 4
            else:
                ret = 5
            mx = str(number[2])
        elif len(set(number)) == 5:
            if number[4] == number[0]+4 or number == [1, 10, 11, 12, 13]:
                if len(set(suit)) == 1:
                    ret = 6
                else:
                    ret = 7
                for i in lst:
                    if str(number[4]) in i:
                        mx = i
    if mx[0] in 'pqrs':
        if 1 <= eval(mx[1:]) <= 2:
            mx = mx[0]+str(mx[1:])
    return ret, mx


def preview(loc, lst):
    global img
    canvas.delete(lst[loc])
    canvas.create_image(10+loc*(card_width-20), screen_height*7//10,
                        image=img[loc], anchor='nw', tags=lst[loc])


img_c = []


def show_player_status():
    global r
    status_width = 20
    status_height = 2
    player_width = screen_width*11//13+10
    player1 = tk.Label(window, bg='red', fg='white',
                       text=r['player1']['name'], anchor='nw', bd=2)
    c_1 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
    for i in range(eval(r['player1']['number'])):
        c_1.create_image(20+i*20, 35, image=img_p, tags='c')
    c_1.place(x=player_width-8, y=120)
    player1.place(x=player_width, y=100)
    player2 = tk.Label(window, bg="red", fg='white',
                       text=r['player2']['name'], anchor='nw', bd=2)
    c_2 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
    for i in range(eval(r['player2']['number'])):
        c_2.create_image(20+i*20, 35, image=img_p, tags='c')
    c_2.place(x=player_width-8, y=220)
    player2.place(x=player_width, y=200)
    player3 = tk.Label(window, bg="red", fg='white',
                       text=r['player3']['name'], anchor='nw', bd=2)
    c_3 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
    for i in range(eval(r['player3']['number'])):
        c_3.create_image(20+i*20, 35, image=img_p, tags='c')
    c_3.place(x=player_width-8, y=320)
    player3.place(x=player_width, y=300)
    player4 = tk.Label(window, bg="red", fg='white',
                       text=r['player4']['name'], anchor='nw', bd=2)
    c_4 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
    for i in range(eval(r['player4']['number'])):
        c_4.create_image(20+i*20, 35, image=img_p, tags='c')
    c_4.place(x=player_width-8, y=420)
    player4.place(x=player_width, y=400)
    window.update()
    turn = r['turn']
    if turn == r['player1']['name']:
        player1.configure(bg='green')
    elif turn == r['player2']['name']:
        player2.configure(bg='green')
    elif turn == r['player3']['name']:
        player3.configure(bg='green')
    elif turn == r['player4']['name']:
        player4.configure(bg='green')


def show_current_card(lst):
    show_player_status()
    global img_c
    img_c = []
    if lst == ['P']:
        return 0
    for i in lst:
        img_pil = Image.open(str(i)+'.png')
        img_c.append(ImageTk.PhotoImage(img_pil))
    for i in range(len(img_c)):
        canvas.create_image((screen_width*11//13)/2-(len(img_c)/2-i)*card_width,
                            screen_height*3//10, image=img_c[i], anchor='nw', tags="current_"+lst[i])


img = []


def game_over():
    global bt_back, screen_height, screen_width, menu_button_height, menu_button_width
    loss_img = Image.open('game_over.png')
    loss_img = ImageTk.PhotoImage(loss_img)
    canvas.pack_forget()
    bt_pass.pack_forget()
    bt_send.pack_forget()
    back.place(x=screen_width*11//13+20, y=screen_height*4//5)
    canvas1.create_image(screen_width*11/13//2,
                         screen_height//2, image=loss_img)
    canvas1.create_text(screen_width*11/13//2, screen_height*5 //
                        6, text="the winner is "+r['win'], fill="white")

    canvas1.place(x=0, y=0)
    while 1:
        window.update()


def Pass():
    global current_card, room_name, name
    requests.get(url+"?send=1&pass=1&room="+room_name +
                 "&name="+name+"&card="+current_card)


current_card = []
r = ''


def refwait():
    global r, name
    r = eval(requests.get(url+"?name="+name+"&room="+room_name+"&wait=1").text)
    try:
        if r['win'] != name:
            game_over()
    except:
        pass
    show_player_status()


def show_card(lst):
    global img, choosed, name, room_name, current_card
    requests.get(url+"?room="+room_name+"&name=" +
                 name+"&card_num="+str(len(card)))
    global r
    hidemenu()
    img = []
    for i in lst:
        img_pil = Image.open(str(i)+'.png')
        img.append(ImageTk.PhotoImage(img_pil))
    for i in range(len(lst)):
        canvas.create_image(10+i*(card_width-20), screen_height*8//10,
                            image=img[i], anchor='nw', tags=lst[i])
    canvas.place(x=0, y=0)

    last = 0
    t = int(time.time())
    r = eval(requests.get(url+"?name="+name+"&room="+room_name+"&wait=1").text)
    current_card = r['card']
    show_current_card(eval(current_card))

    bt_send.configure(state="disabled", bg='red')
    if eval(current_card) == ['P']:
        bt_pass.configure(state="disabled", bg="red")
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
        if t+1 < int(time.time()):
            threading.Thread(target=refwait).start()
            t = int(time.time())
        if current_card != r['card']:
            for i in eval(current_card):
                canvas.delete(["current_"+i])
            current_card = r['card']
            show_current_card(eval(current_card))

        if r['turn'] == name:
            bt_send.place(x=screen_width*12//14, y=screen_height*8//10)
            bt_pass.place(x=screen_width*13//14, y=screen_height*8//10)
            text_turn.place_forget()
        else:
            bt_send.place_forget()
            bt_pass.place_forget()
            text_turn.place(x=screen_width*12//14, y=screen_height*8//10)
        if lst == []:
            win()
        try:
            r['win']
            game_over()
            break
        except:
            pass
        window.update()


def win():
    global name, room_name
    requests.get(url+"?room="+room_name+"&win="+name)
    win_img = Image.open('win.png').resize((500, 500))
    win_img = ImageTk.PhotoImage(win_img)
    canvas1.create_image(screen_width*11/13//2,
                         screen_height//2, image=win_img)
    canvas.place_forget()
    canvas1.place(x=0, y=0)
    bt_pass.place_forget()
    bt_send.place_forget()
    back.place(x=screen_width*11//13+20, y=screen_height*4//5)
    window.mainloop()
card = []


def start_game():
    global room_name, name, card
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
        r = eval(r.text)
        card = r['card']
    elif r['is_exist'] == "true":
        errormsg("Joined!")
        card = r['card']
    elif r['is_exist'] == 'full':
        errormsg("The room is full")
        entry_name.delete(0, tk.END)
        entry_room_name.delete(0, tk.END)
        start()
    print(card)
    card = eval(card)
    if 'p3' in card:
        requests.get(url+"?first="+name+"&room="+room_name)
        bt_pass.configure(state="disabled", bg="red")
    show_card(card)


room_name = ''
name = ''


window = tk.Tk()
window.attributes('-fullscreen', True)
window.configure(bg="black")

window.title("大老二")
title_menu = tk.Label(window, text="Deuces2.0beta",
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
bt_quit = tk.Button(window, width=menu_button_width, height=menu_button_height,
                    text='QUIT', bg='green', fg='white', command=lambda :os.system("taskkill /f /im Python.exe" ))

bt_back = tk.Button(window, width=menu_button_width, height=menu_button_height,
                    text='BACK', bg='green', fg='white', command=menu)
back = tk.Button(window, width=menu_button_width//2, height=menu_button_height,
                     text='EXIT', bg='green', fg='white', command=lambda:os.system('taskkill /f /im Python.exe'))
text_name = tk.Label(div_menu, text="Your nickname", bg="black",
                     fg="white", bd=0, font=("Arial", 18))
entry_name = tk.Entry(div_menu, width=menu_button_width, justify="center")

bt_join_room = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                         text='JOIN', bg='green', fg='white', command=join_room)
text_option = tk.Label(div_menu, text="You have no option but to go back", bg="black",
                       fg="white", bd=0, font=("Arial", 18))
text_console = tk.Entry(div_menu, width=menu_button_width, justify="center")
bt_send = tk.Button(window, width=10, height=10,
                    text='SEND', bg='green', fg='white', command=send)
text_room_name = tk.Label(div_menu, text="Room name", bg="black",
                          fg="white", bd=0, font=("Arial", 18))
entry_room_name = tk.Entry(div_menu, width=menu_button_width, justify="center")
canvas = tk.Canvas(width=screen_width*11//13, height=screen_height,
                   bg="black", borderwidth=0)
card_width = 1850//13
bt_pass = tk.Button(window, width=10, height=10,
                    text='PASS', bg='green', fg='white', command=Pass)
text_turn = tk.Label(div_menu, text="It's not your turn", bg="black",
                     fg="white", bd=0, font=("Arial", 18))
bt_send.configure(state="disabled", bg='red')

img_p_o = Image.open('fold.png')
img_p_o = img_p_o.resize((21, 30))
img_p = ImageTk.PhotoImage(img_p_o)
canvas1 = tk.Canvas(width=screen_width*11//13, height=screen_height,
                    bg="black", borderwidth=0)
player1 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)
player2 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)
player3 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)
player4 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)
c_1 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
c_2 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
c_3 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
c_4 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
menu()
window.mainloop()

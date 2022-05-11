# card_game
from PIL import Image, ImageTk
import pyautogui
import socket
import random
import tkinter as tk
import time
import threading
window = tk.Tk()
window.attributes('-fullscreen', True)
window.configure(bg="black")
current_status = [1, 'p', 3]
choosed = []
tmps = []
choosed_img = []
img = []
ip = ''
player_card = []
player_ip = []
player_name = []
current_card = ['p3']
current_order = 0
choosed_status = []
order = 0
port = 0
start=0
player=1
def hidemenu():
    hidelst = [bt_option, bt_start, bt_quit, bt_join, bt_host, bt_back, text_option,
               text_name, text_ip, text_port, entry_name, entry_ip, entry_port, bt_creat_room, bt_join_room]
    for i in hidelst:
        i.pack_forget()


def start():
    hidemenu()
    bt_join.pack()
    bt_host.pack()
    bt_back.pack()


def quit():
    exit()


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


def join():
    hidemenu()
    text_name.pack()
    entry_name.pack()
    text_ip.pack()
    entry_ip.configure(state="normal")
    entry_ip.pack()
    text_port.pack()
    entry_port.insert(0, "8888")
    entry_port.pack()
    bt_join_room.pack()
    bt_back.pack()


def host():
    hidemenu()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    text_name.pack()
    entry_name.pack()
    text_ip.pack()
    entry_name.delete(0, tk.END)
    entry_port.delete(0, tk.END)
    entry_ip.delete(0, tk.END)
    entry_name.insert(0, "123")
    entry_ip.insert(0, ip)
    entry_ip.configure(state="disabled")

    entry_ip.pack()
    text_port.pack()
    entry_port.insert(0, "8888")
    entry_port.pack()
    bt_creat_room.pack()
    bt_back.pack()


def get_text(obj):
    return obj.get()


def errormsg(msg):
    text_console.delete(0, tk.END)
    text_console.insert(0, msg)
    text_console.pack()


def creat_room():
    ip = get_text(entry_ip)
    name = get_text(entry_name)
    port = get_text(entry_port)
    if name == '':
        errormsg("please enter a name!")
        host()
    elif port == '':
        errormsg("please enter port!")
        host()
    elif ip == '':
        errormsg("please enter ip address!")
        host()
    else:
        host_game(name, ip, port)


def preview_card(loc, lst, img):
    global card_width, choosed
    if lst[loc] not in choosed:
        canvas.delete([lst[loc]])
        canvas.create_image(10+loc*(card_width-20), 800-20,
                            image=img[loc], anchor='nw', tags=str(lst[loc]))
    return loc


def show_choose(img, lst, ind):
    global choosed
    canvas.delete([lst[ind]])
    canvas.create_image(10+ind*(card_width-20), 800-100,
                        image=img[ind], anchor='nw', tags=str(lst[ind]))


def check_type():
    global choosed
    lst = choosed
    suit_lst = []
    num_lst = []
    for i in lst:
        suit_lst.append(i[0])
        num_lst.append(eval(i[1:]))
    num_lst.sort()
    suit_lst.sort()
    if len(lst) == 1:
        return [1, suit_lst[0], num_lst[0]]  # 單張
    elif len(lst) == 2:
        if len(set(num_lst)) == 1:
            return [2, suit_lst[1], num_lst[1]]  # pair
        else:
            return [0, 'a', -1]
    elif len(lst) == 3:
        if len(set(num_lst)) == 1:
            return [3, suit_lst[0], num_lst[0]]  # 條
        else:
            return [0, 'a', -1]
    elif len(lst) == 5:
        if num_lst == list(range(num_lst[0], num_lst[-1]+1)) or num_lst == [1, 10, 11, 12, 13]:
            if len(set(suit_lst)) == 1:
                return [4, suit_lst[4], num_lst[4]]  # 同花
            else:
                return [5, suit_lst[4], num_lst[4]]  # 順子
        elif len(set(num_lst)) == 2:
            if num_lst[2] == num_lst[3] and num_lst[2] == num_lst[1]:
                return [6, suit_lst[2], num_lst[2]]  # 鐵支
            else:
                return [7, suit_lst[2], num_lst[2]]  # 葫蘆
        else:
            return [0, 'a', -1]
    else:
        return [0, 'a', -1]


def check():
    global current_status, choosed_status
    current_status_t = current_status
    if current_status_t[2] < 3:
        current_status_t[2] += 13
    choosed_status = check_type()
    if 0 < choosed_status[2] < 3:
        choosed_status[2] += 13
    if current_status_t[0] == choosed_status[0] and ((choosed_status[2] > current_status_t[2]) or ((choosed_status[2]) == current_status_t[2] and ord(choosed_status[1]) > ord(current_status_t[1]))):
        return True
    elif ((choosed_status[0] == 6) or (choosed_status[0] == 4)) and current_status_t[0] != 4:
        return True
    else:
        return False

def show_card(ip):
    # bt_send.pack()
    global card_width, choosed, tmps, player_card, img, current_card
    for i in player_card[3]:
        img_pil = Image.open(str(i)+'.png')
        img.append(ImageTk.PhotoImage(img_pil))
    for i in range(len(player_card[3])):
        canvas.create_image(10+i*(card_width-20), 800,
                            image=img[i], anchor='nw', tags=player_card[3][i])
        canvas.pack()
    button = ImageTk.PhotoImage(Image.open('button.png'))
    last = 0
    
    while True:
        mouse_x, mouse_y = pyautogui.position()
        loc = (mouse_x-10)//(card_width-20)
        if (screen_width*9//10 <= mouse_x <= screen_width*9//10+80) and (screen_height*5//6 <= mouse_y <= screen_height*5//6+80):
            if order == current_order:
                canvas.bind("<Button-1>", lambda x: send())
            else:
                pass  # not your turn
        elif 0 <= loc < len(player_card[3]):
            canvas.bind(
                '<Button-1>', lambda x: tmps.append([player_card[3][loc], loc]))
        if (last != loc):
            if len(player_card[3]) > last >= 0 and player_card[3][last] not in choosed:
                canvas.delete(player_card[3][last])
                canvas.create_image(
                    10+last*(card_width-20), 800, image=img[last], anchor='nw', tags=str(player_card[3][last]))
            if 0 <= loc < len(player_card[3]):
                last = preview_card(loc, player_card[3], img)
        tmp = ''
        if tmps != []:
            tmp = tmps[0][0]
            ind = tmps[0][1]
            tmps = []
            print(ind)
        if tmp == '':
            pass
        elif tmp in choosed:
            choosed.remove(tmp)
            choosed_img.remove(ind)
            canvas.delete([tmp])
            canvas.create_image(10+ind*(card_width-20),
                                800-20, image=img[ind], anchor='nw', tags=tmp)
        else:
            choosed.append(tmp)
            choosed_img.append(ind)
            canvas.delete([tmp])
            show_choose(img, player_card[3], ind)

        window.update()

        if check():
            canvas.create_image(screen_width*9//10, screen_height*5//6-40,
                                image=button, anchor='nw', tags="send")
        else:
            canvas.delete(['send'])
        window.update()


def host_game(name, ip, pt):
    global player_card, player_ip, player_name, port,current_order, player
    port = pt
    hidemenu()
    port = eval(port)
    text_console.insert(0, "waiting player to join")
    text_console.pack()
    card = []
    for i in "pqrs":
        for j in range(1, 14):
            card.append(i+str(j))
    random.shuffle(card)
    player_card.append(card[:13])
    player_card.append(card[13:26])
    player_card.append(card[26:39])
    player_card.append(card[39:52])
    window.update()
    
    div_menu.pack_forget()
    player_card[3].sort()
    for i in range(4):
        if "p3" in player_card[i]:
            current_order = i
    
    canvas.pack()
    show_card(ip)


def join_room():
    ip = get_text(entry_ip)
    port = get_text(entry_port)
    name = get_text(entry_name)
    if name == '':
        errormsg("please enter a name!")
        join()
    elif port == '':
        errormsg("please enter port!")
        join()
    elif ip == '':
        errormsg("please enter ip address!")
        join()
    else:
        join_game(name, ip, port)


def join_game(name, ip, pt):
    global player_card, order, player_ip, player_name, port
    port = pt
    
    
    show_card(ip)


def send():
    global choosed, player_card, img, choosed_img, port, choosed_status, port, current_card, current_order, current_status
    button_down = ImageTk.PhotoImage(Image.open('buttondown.png'))
    canvas.delete(['send'])
    canvas.create_image(screen_width*9//10, screen_height*5//6-26,
                        image=button_down, anchor='nw', tags="send")
    window.update()
    time.sleep(0.3)
    button = ImageTk.PhotoImage(Image.open('button.png'))
    canvas.delete(['send'])
    canvas.create_image(screen_width*9//10, screen_height*5//6-40,
                        image=button, anchor='nw', tags="send")
    for i in choosed:
        player_card[3].remove(i)
        canvas.delete([i])
    for i in choosed_img:
        img.remove(img[i])
    canvas.pack()
    choosed = []
    window.update()
    current_order = order+1
    current_card = choosed
    current_status = choosed_status
    

# menu介面
window.title("大老二")
title_menu = tk.Label(window, text="Deuces",
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

bt_join = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                    text='JOIN A GAME', bg='green', fg='white', command=join)
bt_host = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                    text='HOST A GAME', bg='green', fg='white', command=host)
bt_back = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                    text='BACK', bg='green', fg='white', command=menu)
text_ip = tk.Label(div_menu, text="ip address", bg="black",
                   fg="white", bd=0, font=("Arial", 18))
entry_ip = tk.Entry(div_menu, width=menu_button_width, justify="center")
text_name = tk.Label(div_menu, text="Your nickname", bg="black",
                     fg="white", bd=0, font=("Arial", 18))
entry_name = tk.Entry(div_menu, width=menu_button_width, justify="center")
bt_creat_room = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                          text='CREATE', bg='green', fg='white', command=creat_room)
text_port = tk.Label(div_menu, text="port", bg="black",
                     fg="white", bd=0, font=("Arial", 18))
entry_port = tk.Entry(div_menu, width=menu_button_width, justify="center")
bt_join_room = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                         text='JOIN', bg='green', fg='white', command=join_room)
text_option = tk.Label(div_menu, text="You have no option but to go back", bg="black",
                       fg="white", bd=0, font=("Arial", 18))
text_console = tk.Entry(div_menu, width=menu_button_width, justify="center")
canvas = tk.Canvas(width=screen_width, height=screen_height,
                   bg="black", borderwidth=0)
bt_send = tk.Button(canvas, width=10, height=10,
                    text='SEND', bg='green', fg='white', command=send)
card_width = 1850//13
menu()
window.mainloop()

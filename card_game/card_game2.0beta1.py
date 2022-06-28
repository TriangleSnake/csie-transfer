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

def hidemenu():#每進到一個新介面，就要先將原本介面上的元素刪除(再放上新介面的元素)
    pack_hidelst = [bt_option, bt_start, bt_quit, bt_back, text_option,
               text_name, entry_name, text_room_name, entry_room_name, bt_join_room]
    place_hidelst=[canvas, canvas1, bt_send, bt_pass, player1, player2, player3, player4,back,c_1,c_2,c_3,c_4]
    for i in pack_hidelst:
        i.pack_forget()
    for i in place_hidelst:    
        i.place_forget()


def start():#設計按下START後的介面(伺服器連線設定頁)
    hidemenu()
    text_name.pack()
    entry_name.pack()
    text_room_name.pack()
    entry_room_name.pack()
    bt_join_room.pack()
    bt_back.pack()
    entry_name.insert(0, "123")
    entry_room_name.insert(0, "123")


def option():#設計按下OPTION後的介面:裡面啥都沒有
    hidemenu()
    text_option.pack()
    bt_back.pack()


def menu():#設計MENU介面
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


def join_room():#準備丟給伺服器的資料
    global room_name, name
    name = entry_name.get()
    room_name = entry_room_name.get()

    if name == '':#檢查名稱不得為空
        errormsg("please enter a name!")
        start()
    elif room_name == '':
        errormsg("please enter room name!")
        start()
    else:
        start_game()


def send():#設定SEND按鈕的指令:傳送已選中的合法的牌至後台伺服器
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


def choose(card, lst, loc):#設計"選牌"動作
    global choosed, current_card

    if card in choosed:#若牌不再被選中，將牌"放"回去
        canvas.delete(lst[loc])
        canvas.create_image(10+loc*(card_width-20), screen_height*7//10,
                            image=img[loc], anchor='nw', tags=lst[loc])
        choosed.remove(card)
    else:
        #若牌被選中，將牌"拉"出來:刪除原圖片並在正上方重新建立
        choosed.append(card)
        canvas.delete(lst[loc])
        canvas.create_image(10+loc*(card_width-20), screen_height*6//10,
                            image=img[loc], anchor='nw', tags=lst[loc])
    #合法牌才能出，不合法時SEND按鈕即失效
    if check() == True:
        bt_send.configure(state="normal", bg='green')
    else:
        bt_send.configure(state="disabled", bg='red')


def check():#判定牌是否和檯面上牌型相同且大於檯面上的牌
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


def checktype(lst):#判定牌是否合法，回傳牌型和大小，再給上面的CHECK函式判斷是否大於牌面上的牌
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

    # 單張
    if len(lst) == 1:  
        ret = 1
        mx = lst[0]

    # pair
    elif len(lst) == 2:  
        if len(set(number)) == 1:
            ret = 2
            mx = lst[1]

    # 條
    elif len(lst) == 3:  
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
    try:
        print(mx,type(mx))
        if 1<=eval(mx)<=2:
            mx=str(eval(mx)+13)
    except:
        print(mx,type(mx))
        if 1 <= eval(mx[1:]) <= 2:
            mx = mx[0]+str(eval(mx[1:])+13)
            print(mx)
    return ret, mx


def preview(loc, lst):#設計"看卡牌"動作:將牌"稍微"往上拉，刪除原圖片並在正上方重新建立
    global img
    canvas.delete(lst[loc])
    canvas.create_image(10+loc*(card_width-20), screen_height*7//10,
                        image=img[loc], anchor='nw', tags=lst[loc])


img_c = []


def show_player_status():#顯示其他玩家的狀態
    global r
    status_width = 20
    status_height = 2
    player_width = screen_width*11//13+10

    #顯示玩家的名字
    player1 = tk.Label(window, bg='red', fg='white',
                       text=r['player1']['name'], anchor='nw', bd=2)
    #各玩家所剩下的牌數(圖形化)
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

    #輪到誰的回合:將該玩家標示為綠色(其他為紅色)
    turn = r['turn']
    if turn == r['player1']['name']:
        player1.configure(bg='green')
    elif turn == r['player2']['name']:
        player2.configure(bg='green')
    elif turn == r['player3']['name']:
        player3.configure(bg='green')
    elif turn == r['player4']['name']:
        player4.configure(bg='green')


def show_current_card(lst):#在牌桌上顯示遊戲中上一張所出的牌
    show_player_status()
    global img_c
    img_c = []

    #如果所有玩家都pass，則清空上一張牌(即可出任意牌)
    if lst == ['P']:
        return 0

    for i in lst:
        img_pil = Image.open(str(i)+'.png')
        img_c.append(ImageTk.PhotoImage(img_pil))
    for i in range(len(img_c)):
        canvas.create_image((screen_width*11//13)/2-(len(img_c)/2-i)*card_width,
                            screen_height*3//10, image=img_c[i], anchor='nw', tags="current_"+lst[i])


img = []


def game_over():#當觸發失敗條件時的後續動作
    global bt_back, screen_height, screen_width, menu_button_height, menu_button_width
    #顯示失敗圖片
    loss_img = Image.open('game_over.png')
    loss_img = ImageTk.PhotoImage(loss_img)
    #隱藏原介面上的其他元素
    canvas.pack_forget()
    bt_pass.pack_forget()
    bt_send.pack_forget()
    #放置back按鈕
    back.place(x=screen_width*11//13+20, y=screen_height*4//5)
    canvas1.create_image(screen_width*11/13//2,
                         screen_height//2, image=loss_img)
    #告知勝利玩家
    canvas1.create_text(screen_width*11/13//2, screen_height*5 //
                        6, text="the winner is "+r['win'], fill="white")

    canvas1.place(x=0, y=0)
    while 1:
        window.update()


def Pass():#設定pass指令:通知伺服器換下一個玩家
    global current_card, room_name, name
    requests.get(url+"?send=1&pass=1&room="+room_name +
                 "&name="+name+"&card="+current_card)


current_card = []
r = ''


def refwait():#隨時向伺服器確認
    global r, name
    r = eval(requests.get(url+"?name="+name+"&room="+room_name+"&wait=1").text)
    #確認是否已有贏家產生
    try:
        if r['win'] != name:
            game_over()
    except:
        pass
    #確認其他玩家狀態
    show_player_status()


def show_card(lst):#設定遊戲主介面
    global img, choosed, name, room_name, current_card
    requests.get(url+"?room="+room_name+"&name=" +
                 name+"&card_num="+str(len(card)))
    global r
    hidemenu()

    #列出玩家所持有的牌
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
    #請求伺服器牌組和其他玩家狀態
    r = eval(requests.get(url+"?name="+name+"&room="+room_name+"&wait=1").text)
    current_card = r['card']
    show_current_card(eval(current_card))

    bt_send.configure(state="disabled", bg='red')
    if eval(current_card) == ['P']:
        bt_pass.configure(state="disabled", bg="red")
    
    while True:
        #偵測滑鼠所在位置
        window.update()
        mouse_x, mouse_y = pyautogui.position()
        loc = (mouse_x-10)//(card_width-20)#把畫面分成len(lst)個區塊，依照區塊讓牌彈出
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
            threading.Thread(target=refwait).start()#利用多執行續每隔一秒向伺服器請求資訊
            t = int(time.time())
        if current_card != r['card']:#若按了三次暫停，則可任意出牌
            for i in eval(current_card):
                canvas.delete(["current_"+i])
            current_card = r['card']
            show_current_card(eval(current_card))

        #若輪到自己回合，顯示send和pass按鈕；反之則不顯示
        if r['turn'] == name:
            bt_send.place(x=screen_width*12//14, y=screen_height*8//10)
            bt_pass.place(x=screen_width*13//14, y=screen_height*8//10)
            text_turn.place_forget()
        else:
            bt_send.place_forget()
            bt_pass.place_forget()
            text_turn.place(x=screen_width*12//14, y=screen_height*8//10)

        #檢查勝利條件是否成立
        if lst == []:
            win()
        try:#檢查是否有玩家贏了
            r['win']
            game_over()
            break
        except:
            pass
        window.update()


def win():#檢查勝利條件是否成立及後續動作
    global name, room_name
    #向伺服器確認勝利玩家
    requests.get(url+"?room="+room_name+"&win="+name)
    #顯示勝利圖片
    win_img = Image.open('win.png').resize((500, 500))
    win_img = ImageTk.PhotoImage(win_img)
    canvas1.create_image(screen_width*11/13//2,
                         screen_height//2, image=win_img)
    #隱藏介面上其他元素，並顯示back按鈕
    canvas.place_forget()
    canvas1.place(x=0, y=0)
    bt_pass.place_forget()
    bt_send.place_forget()
    back.place(x=screen_width*11//13+20, y=screen_height*4//5)
    window.mainloop()


card = []


def start_game():#當遊戲開始的動作
    global room_name, name, card
    #設定伺服器開始
    r = requests.get(url+"?start=1&room="+room_name+"&name="+name).text
    print(r)
    r = eval(r)
    print(r)
    card = []
    if r['is_exist'] == "false":#若指定的房間不存在，自動創建房間並洗牌
        errormsg("The room doesn't exist, creating "+room_name)
        for i in 'pqrs':
            for j in range(1, 14):
                card.append(i+str(j))
        random.shuffle(card)
        r = requests.get(url+"?create_room="+room_name +
                         "&name="+name+"&card="+str(card))
        r = eval(r.text)
        card = r['card']
    elif r['is_exist'] == "true":#加入已存在的房間並發牌
        errormsg("Joined!")
        card = r['card']
    elif r['is_exist'] == 'full':#不可加入已滿的房間
        errormsg("The room is full")
        entry_name.delete(0, tk.END)
        entry_room_name.delete(0, tk.END)
        start()
    print(card)
    card = eval(card)
    #將發牌回合分配給擁有梅花3的玩家
    if 'p3' in card:
        requests.get(url+"?first="+name+"&room="+room_name)
        bt_pass.configure(state="disabled", bg="red")
    show_card(card)


room_name = ''
name = ''

#設定啟動程式時的介面
window = tk.Tk()
window.attributes('-fullscreen', True)#全螢幕執行
window.configure(bg="black")#背景設定黑色
window.title("大老二")
title_menu = tk.Label(window, text="Deuces2.0beta",
                      background="white", font=('Arial', 40))
screen_width = window.winfo_screenwidth()#找出顯示器長寬像素
screen_height = window.winfo_screenheight()
div_menu = tk.LabelFrame(window, width=40, height=100,
                         background="black")

#定義遊戲大廳介面上的按鈕
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

#定義按下START後的介面(伺服器連線設定頁)的元素
text_name = tk.Label(div_menu, text="Your nickname", bg="black",
                     fg="white", bd=0, font=("Arial", 18))
entry_name = tk.Entry(div_menu, width=menu_button_width, justify="center")

bt_join_room = tk.Button(div_menu, width=menu_button_width, height=menu_button_height,
                         text='JOIN', bg='green', fg='white', command=join_room)

#定義按下OPTION後的介面的元素
text_option = tk.Label(div_menu, text="You have no option but to go back", bg="black",
                       fg="white", bd=0, font=("Arial", 18))
text_console = tk.Entry(div_menu, width=menu_button_width, justify="center")

#定義遊戲主介面的元素(按鈕)
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

#蓋牌的圖片
img_p_o = Image.open('fold.png')
img_p_o = img_p_o.resize((21, 30))
img_p = ImageTk.PhotoImage(img_p_o)
canvas1 = tk.Canvas(width=screen_width*11//13, height=screen_height,
                    bg="black", borderwidth=0)

#定義遊戲主介面的元素(玩家狀態)
player1 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)#四個玩家名稱
player2 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)
player3 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)
player4 = tk.Label(window, bg='red', fg='white',
                   text="NONE", anchor='nw', bd=2)
c_1 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')#四個玩家的狀態列
c_2 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
c_3 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')
c_4 = tk.Canvas(window, width=screen_width*2//13-5, height=70, bg='black')

#開始執行主迴圈
menu()
window.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import datetime as dt
import pymysql
import cv2
import DES_Algorithm2 as DES
import numpy as np
from socket import *

def db_connect(): # db 연결
    global conn
    global cur


    host = host_input.get()
    user = user_input.get()
    pw = pw_input.get()
    db_name = db_input.get()

    host_input.delete(0, 'end')
    user_input.delete(0, 'end')
    pw_input.delete(0, 'end')
    db_input.delete(0, 'end')

    try :
        conn = pymysql.connect(host=host, user=user, password=pw, db=db_name, charset='utf8')
        cur = conn.cursor()
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        log.configure(state='normal')
        log.insert('end',now + " : " + "Database connected" + "\n")
        log.configure(state='disabled')
        
        status_red.place_forget()
        status_green.place(x = 660, y = 20)
                
        db_onoff.configure(text = 'Connected')
    
    except :
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        log.configure(state='normal')
        log.insert('end',now + " : " +  "Could not connect to Database" + "\n")
        log.configure(state='disabled')

def db_close() : # db 연결해제
    
    try :
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        conn.close()
        log.configure(state='normal')
        log.insert('end',now + " : " +  "Database connection closed" + "\n")
        log.configure(state='disabled')
        db_onoff.configure(text = 'Closed')

        status_green.place_forget()
        status_red.place(x = 660, y = 20)
    
    except :
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        log.configure(state='normal')
        log.insert('end',now + " : " +  "There is no connection" + "\n")
        log.configure(state='disabled')

    
def select() : # 파일 선택 및 미리보기
    global photo
    global filename
    global f_split

    ####이미지 띄우기####
    filename = filedialog.askopenfilename(initialdir='./png',title='파일선택', filetypes=(('png files','*.png'),('jpg files','*.jpg'),('all files','*.*'))) # 파일탐색기로 경로따옴
    image = Image.open(filename) # filename으로 이미지 오픈
    resized_image = image.resize((350,350)) # 불러온 이미지 크기 조정
    photo = ImageTk.PhotoImage(resized_image)
    pre_img.configure(image=photo) # 미리보기 띄움

    ####파일 정보 출력####
    file_stats = os.stat(filename) # 파일 정보
    file_size = str(file_stats.st_size / (1024 * 1024)) # 파일정보에서 사이즈만
    size_lb.configure(text = file_size[0:4] + "MB") # 사이즈 출력
    f_split = filename.split("/") # 경로 split 배열
    dir_dis.configure(text = ('/').join(f_split[0:-1])) # 경로 출력
    fn.configure(text = f_split[-1]) # 파일 이름 출력

    ## 암호화 / 복호화 버튼 활성화 ##
    file_encrypt['state'] = tk.NORMAL
    file_decrypt['state'] = tk.NORMAL

    
def clear() : # 로그창 비우기
    log.configure(state='normal')
    log.delete("1.0","end")
    log.configure(state='disabled')

def encrpyt_image():
    global CBC_encrypted_img
    now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
    log.configure(state='normal')
    log.insert('end',now + " : " +  "Start Encryption" + "\n")
    log.configure(state='disabled')
    
    img = cv2.imread(filename)  # 이미지 읽기
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB 순서 변경
    img = cv2.resize(img, (128, 128))  # 이미지 크기 조정
    img_arr = np.array(img)  # 배열로 변환
    CBC_encrypted_img = DES.DES_CBC(img_arr, [1,2,3,4,5,6,7,8], round=16)

    now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
    log.configure(state='normal')
    log.insert('end',now + " : " +  "Encryption Complete" + "\n")
    log.configure(state='disabled')

    file_encrypt['state'] = tk.DISABLED
    file_decrypt['state'] = tk.DISABLED

    size_lb.configure(text = '')
    dir_dis.configure(text = '')
    fn.configure(text = '')
    pre_img.config(image='')
    
    
    

def decrypt_image():
    DES.DES_CBC_decrypt(CBC_encrypted_img, [1,2,3,4,5,6,7,8], round=16)

    file_encrypt['state'] = tk.DISABLED
    file_decrypt['state'] = tk.DISABLED

def sock_conncect() :
    addr = ip_input.get()
    port = int(port_input.get())
    addr_info.configure(text = f"Server is running as {addr}:{port}")
    ip_input.delete(0, 'end')
    port_input.delete(0, 'end')
    try :
        serverSock = socket(AF_INET, SOCK_STREAM) # 소켓연결
        serverSock.bind((addr, port))
        serverSock.listen(1)
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        log.configure(state='normal')
        log.insert('end',now + " : " +  "Server running" + "\n")
        log.insert('end',now + " : " +  "Waiting for client..." + "\n")
        log.configure(state='disabled')
    except :
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        log.configure(state='normal')
        log.insert('end',now + " : " +  "Could not run server" + "\n")
        log.configure(state='disabled')

    


# 메인 창 설정
window = tk.Tk()
window.geometry('1200x800')
window.title('Server')
window.resizable(False, False)

#서버 프레임
server_f = tk.Frame(window, relief='sunken', borderwidth=1)
ip_input = tk.Entry(server_f)
ip_input_lb = tk.Label(server_f, text = "IP : ")
port_input = tk.Entry(server_f)
port_input_lb = tk.Label(server_f, text = "Port : ")
addr_info = tk.Label(server_f, text = '')


ip_input.place(x = 45, y = 15, width = 140)
ip_input_lb.place(x = 10, y = 15)
port_input.place(x = 250, y = 15, width = 50)
port_input_lb.place(x = 190, y = 15)
addr_info.place(x = 800, y = 15, width = 350)

start_server = tk.Button(server_f, text = 'Run', command = sock_conncect)
start_server.place(x = 45, y = 60, width = 205, height = 30)


#로그 프레임 740, 400
log_f = tk.Frame(window, relief='sunken', borderwidth=1)
log_check = tk.Button(log_f, text = 'Check Logs', command = input)
log_clear = tk.Button(log_f, text = 'Clear Logs', command = clear)
log = scrolledtext.ScrolledText(log_f)
log.configure(state='disabled')

log.place(x = 20, y = 100, width = 700, height = 290)
log_check.place(x = 100 , y = 25, width = 170, height = 50)
log_clear.place(x = 470 , y = 25, width = 170, height = 50)

#이미지 프레임 400, 400
img_f = tk.Frame(window, relief='sunken', borderwidth=1)
photo = tk.PhotoImage(file='')
pre_img=tk.Label(img_f, text = "Image preview")
pre_img.place(x = 25, y = 25, width = 350, height = 350) 

#파일 프레임 400, 200
file_f = tk.Frame(window, relief='sunken', borderwidth=1)
file_transfer = tk.Button(file_f, text = 'Transfer File')
file_select = tk.Button(file_f, text = 'Select FIle', command=select)

file_encrypt = tk.Button(file_f, text = 'Encrypt Image', state=tk.DISABLED, command=encrpyt_image)
file_decrypt = tk.Button(file_f, text = 'Decrypt Image', state=tk.DISABLED, command=decrypt_image)

dir_lb = tk.Label(file_f, text = "Directory : ")
dir_dis = tk.Label(file_f, text = '')
fn_lb = tk.Label(file_f, text = "FileName : ")
fn = tk.Label(file_f, text = '')
fs_lb = tk.Label(file_f, text = "FileSize : ")
size_lb = tk.Label(file_f, text = '')


dir_lb.place(x = 10, y = 20, width = 100, height = 25)
dir_dis.place(x = 100, y = 20, width = 300, height = 25)
fn_lb.place(x = 10, y = 50, width = 100, height = 25)
fn.place(x = 100, y = 50, width = 300, height = 25)
fs_lb.place(x = 10, y = 80, width = 100, height = 25)
size_lb.place(x = 100, y = 80, width = 300, height = 25)

file_select.place(x= 30, y = 120, width = 150, height = 30)
file_transfer.place(x= 220, y = 120, width = 150, height = 30)
file_encrypt.place(x=30, y = 150, width = 150, height= 30)
file_decrypt.place(x=220, y = 150, width = 150, height= 30)

#DB 프레임 740, 200

db_f = tk.Frame(window, relief='sunken', borderwidth=1)

host_input = tk.Entry(db_f)
user_input = tk.Entry(db_f)
pw_input = tk.Entry(db_f)
db_input = tk.Entry(db_f)
make_connect = tk.Button(db_f, text = 'Connect to DB', command=db_connect)
close_connect = tk.Button(db_f, text = 'Close connection', command=db_close)

host_lb = tk.Label(db_f, text = 'Host : ')
user_lb = tk.Label(db_f, text = 'User : ')
pw_lb = tk.Label(db_f, text = 'Password : ')
db_lb = tk.Label(db_f, text = 'Database : ')


red_image = Image.open(r"red_button.png") 
resized_red = red_image.resize((50,50)) 
red = ImageTk.PhotoImage(resized_red)
status_red = tk.Label(db_f, image = red)


green_image = Image.open(r"green_button.png") 
resized_green = green_image.resize((50,50)) 
green = ImageTk.PhotoImage(resized_green)
status_green = tk.Label(db_f, image = green)

status_lb = tk.Label(db_f, text = 'Status', font='30')
db_onoff = tk.Label(db_f, text = 'Closed')

host_input.place(x = 130, y = 23, width = 150, height = 30)
user_input.place(x = 130, y = 68, width = 150, height = 30)
pw_input.place(x = 130, y = 113, width = 150, height = 30)
db_input.place(x = 130, y = 158, width = 150, height = 30)
make_connect.place(x = 315, y = 35, width = 150, height = 50)
close_connect.place(x = 315, y = 125, width = 150, height= 50)

host_lb.place(x = 15, y = 25, width = 90, height = 20)
user_lb.place(x = 15, y = 70, width = 90, height = 20)
pw_lb.place(x = 15, y = 115, width = 90, height = 20)
db_lb.place(x = 15, y = 160, width = 90, height = 20)

status_red.place(x = 660, y = 20)
#status_lb.place(x = 672, y = 15)
db_onoff.place(x = 637, y = 73, width = 100, height = 20)



#위젯

 
server_start = tk.Button(window, text = 'Run Server')


log_lb = tk.Label(window, text = 'Log')
preview = tk.Label(window, text = 'Preview')
server_lb = tk.Label(window, text = 'Server')
file_lb = tk.Label(window, text = 'File Selection')
db_lb = tk.Label(window, text = 'Database')




server_lb.place(x = 40, y = 5, width = 50, height = 30)
file_lb.place(x = 30, y = 135, width = 120, height = 30)
preview.place(x = 30, y = 365, width = 80, height = 30)
log_lb.place(x = 470, y = 365, width = 40, height = 30)
db_lb.place(x = 460, y = 135, width = 80, height = 30)

server_f.place(x = 20, y = 20, width = 1160, height = 100)
file_f.place(x = 20, y = 150, width = 400, height = 200)
img_f.place(x = 20, y = 380, width = 400, height = 400)
log_f.place(x = 440, y = 380, width = 740, height = 400)
db_f.place(x = 440, y = 150, width = 740, height = 200)




window.mainloop()
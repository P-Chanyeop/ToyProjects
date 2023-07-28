from socket import *
from os.path import exists
import sys
import DES as des
from PIL import Image
import numpy as np
import cv2
import time
import pymysql
import datetime as dt


def insertDB(date, string):
    pass

def selectDB():
    pass


#db연결##############
# print("-----Database connect-----")
# id = input("Username : ")
# pw = input("Password : ")
# use = input("Database name : ")
try : # db 연결
    log = pymysql.connect(host = 'localhost', user="root", password="7579", db="des", charset='utf8')
    print("Database connected")
    
except :
    print("Can`t connect to database")
####################

cur = log.cursor() #db 커서 생성

# addr = input("Input IP : ")
serverSock = socket(AF_INET, SOCK_STREAM) # 소켓연결
serverSock.bind(("localhost", 8080))
serverSock.listen(1)
print('클라이언트의 접속을 기다리는중...')
now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
sql = f'INSERT INTO log(date, logs) VALUES("{now}", "서버 시작")'
cur.execute(sql)
log.commit()

connectionSock, addr = serverSock.accept()
now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
sql = f'insert into log(date, logs) values("{now}", "{str(addr)}에서 접속했습니다.")'
cur.execute(sql)
log.commit()

print(str(addr),'에서 접속했습니다.')



if connectionSock:
    filename = connectionSock.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
    filename = filename.decode("utf-8")
    now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
    sql = f'INSERT INTO log(date, logs) VALUES("{now}", "{str(addr)}로 부터 {filename} 요청 받음")'
    cur.execute(sql)
    log.commit()
    print('요청 받은 파일 : ', filename) #파일 이름을 일반 문자열로 변환한다
    data_transferred = 0
    
    select = input('암호화를 하시겠습니까? (y/n)')
    
    if select == 'y':
        # msg = "Encrpyted Image is comming..."
        # connectionSock.send(msg.encode())
        print("이미지를 암호화중....Loading...")
        
        # 복호화 후 이미지 저장
        img = cv2.imread("/Users/pcy/Desktop/무제 폴더/"+ filename)  # 이미지 읽기
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB 순서 변경
        img = cv2.resize(img, (128, 128))  # 이미지 크기 조정
        img_arr = np.array(img)  # 배열로 변환
        

        # print(img_arr)
        des.DES_CBC(img_arr, [1,2,3,4,5,6,7,8], round = 16)
        # ciphertext = np.ascontiguousarray(ciphertext)
        # connectionSock.sendall(ciphertext)

        
        
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        sql = f'INSERT INTO log(date, logs) VALUES("{now}", "{filename} 암호화 완료")'
        cur.execute(sql)
        log.commit()
        print('이미지 암호화 >>> "Encrypted_img.jpg" 이름으로 저장 완료.')
        
        filename = 'Encrypted_img.jpg'

        if not exists('/Users/pcy/Desktop/무제 폴더/' + filename):
            print("no file")
            sys.exit()

        print("파일 %s 전송 시작" % filename)
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        sql = f'INSERT INTO log(date, logs) VALUES("{now}", "{str(addr)}에게 {filename} 전송 시작")'
        cur.execute(sql)
        log.commit()
        
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024) #1024바이트 읽는다
                while data: #데이터가 없을 때까지
                    data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
                    data = f.read(1024) #1024바이트 읽음
                    
            except Exception as ex:
                print(ex)
        print('전송완료 "%s", 전송량 %d' % (filename, data_transferred))
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        sql = f'INSERT INTO log(date, logs) VALUES("{now}", "{str(addr)}에게 {filename} 전송 완료, 전송량 : {data_transferred}")'
        cur.execute(sql)
        log.commit()
        
    if select == 'n':
        print("파일 %s 전송 시작" % filename )
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        sql = f'INSERT INTO log(date, logs) VALUES("{now}", "{str(addr)}에게 {filename} 전송 시작")'
        cur.execute(sql)
        log.commit()
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024) #1024바이트 읽는다
                while data: #데이터가 없을 때까지
                    data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
                    data = f.read(1024) #1024바이트 읽음
                    
            except Exception as ex:
                print(ex)
        print('전송완료 "%s", 전송량 %d' % (filename, data_transferred))
        now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
        sql = f'INSERT INTO log(date, logs) VALUES("{now}", "{str(addr)}에게 {filename} 전송 완료, 전송량 : {data_transferred}")'
        cur.execute(sql)
        log.commit()

print("파일 전송 끝")
now = dt.datetime.now().strftime("%Y/%m/%d %A %H:%M:%S")
sql = f'INSERT INTO log(date, logs) VALUES("{now}", "서버 종료")'
cur.execute(sql)
log.commit()
sys.exit()
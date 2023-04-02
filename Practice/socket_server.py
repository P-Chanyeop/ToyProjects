from socket import *
from os.path import exists
import sys
import DES_Algorithm as des
from PIL import Image
import numpy as np
import cv2
import time

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)
print('클라이언트의 접속을 기다리는중...')
connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속했습니다')

if connectionSock:
    filename = connectionSock.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
    filename = filename.decode("utf-8")
    print('받은 데이터 : ', filename) #파일 이름을 일반 문자열로 변환한다
    data_transferred = 0
    
    select = input('암호화를 하시겠습니까? (y/n)')
    
    if select == 'y':
        print("이미지를 암호화중....Loading...")
        # 복호화 후 이미지 저장
        img = cv2.imread("/Users/pcy/Desktop/works/python/Practice/"+ filename)  # 이미지 읽기
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB 순서 변경
        img = cv2.resize(img, (1000, 1000))  # 이미지 크기 조정
        img_arr = np.array(img)  # 배열로 변환

        des.DES_CBC(img, [1,2,3,4,5,6,7,8], round = 16)
        print('이미지 암호화 >>> "Encrypted_img.jpg" 이름으로 저장 완료.')
        time.sleep(5)
        
        filename = 'Encrypted_img.jpg'

        if not exists('Encrypted_img.jpg'):
            print("no file")
            sys.exit()

        print("파일 %s 전송 시작" % filename)
        
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024) #1024바이트 읽는다
                while data: #데이터가 없을 때까지
                    data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
                    data = f.read(1024) #1024바이트 읽음
                    
            except Exception as ex:
                print(ex)
        print('전송완료 "%s", 전송량 %d' % (filename, data_transferred))
        print(data)
        
    if select == 'n':
        print("파일 %s 전송 시작" % filename )
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024) #1024바이트 읽는다
                while data: #데이터가 없을 때까지
                    data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
                    data = f.read(1024) #1024바이트 읽음
                    
            except Exception as ex:
                print(ex)
        print('전송완료 %s", 전송량 %d' % (filename, data_transferred))
        print(data)

print("파일 전송 끝")
sys.exit()
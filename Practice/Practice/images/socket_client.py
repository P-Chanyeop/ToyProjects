from socket import *
import os
import sys
import DES_Algorithm as des
from PIL import Image
import numpy as np
import cv2


clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('localhost', 8080))

print('연결에 성공했습니다.')
filename = input('전송할 파일 이름을 입력하세요: ')
clientSock.sendall(filename.encode('utf-8'))

data = clientSock.recv(1024)
data_transferred = 0


while(True):
    select = int(input('1. 파일 받기 \n2. 이미지 복호화\n입력>>'))

    if select == 1:
        if not data:
            print('파일 %s 가 서버에 존재하지 않음' % filename)
            sys.exit()

        nowdir = os.getcwd()
        with open(nowdir+"/" + filename, 'wb') as f: #현재dir에 filename으로 파일을 받는다
            try:
                while data: #데이터가 있을 때까지
                    f.write(data) #1024바이트 쓴다
                    data_transferred += len(data)
                    data = clientSock.recv(1024) #1024바이트를 받아 온다
            except Exception as ex:
                print(ex)
        print('파일 "%s" 받기 완료. 전송량 %d' % (filename, data_transferred))

    elif select == 2 :
        print("이미지를 복호화중.....Loading...")
        
        if not data:
            print('파일 %s 가 서버에 존재하지 않음' % filename)
            sys.exit()

        nowdir = os.getcwd()
        with open(nowdir+"/" + filename, 'wb') as f: #현재dir에 filename으로 파일을 받는다
            try:
                while data: #데이터가 있을 때까지
                    f.write(data) #1024바이트 쓴다
                    data_transferred += len(data)
                    data = clientSock.recv(1024) #1024바이트를 받아 온다
            except Exception as ex:
                print(ex)
        print('파일 "%s" 받기 완료. 전송량 %d' % (filename, data_transferred))
        
        img = cv2.imread("/Users/pcy/Desktop/works/python/Practice/Practice/images/"+ filename)  # 이미지 읽기
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # BGR -> RGB 순서 변경
        img = cv2.resize(img, (128, 128))  # 이미지 크기 조정
        img_arr = np.array(img)  # 배열로 변환
        des.DES_CBC_decrypt(img_arr, [1,2,3,4,5,6,7,8], round=1)
        print('암호화된 이미지 복호화 >>> "Decrypted_img" 이름으로 저장 완료.')
        

        # encrpyted_img = des.DES_CBC(img_arr, [1,2,3,4,5,6,7,8], round = 16)
        # 복호화 후 이미지 저장 (DES_CBC_decrypt 함수에 사용한 cv모듈을 사용시 jpg를 변환하는 과정에서 이미지 색상정보가 약간 깨질 가능성이 있다.)
    
        
        
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        break
    
print("파일 전송 끝")
sys.exit()
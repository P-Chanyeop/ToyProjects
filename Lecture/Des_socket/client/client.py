from socket import *
import os
import sys
import DES_Algorithm2 as dess
from PIL import Image
import numpy as np
import cv2

# 이미지를 복호화하는 함수
def decrypt_image(image_path, key, round=16):
    img = Image.open(image_path)  # 이미지 파일 열기
    img_arr = np.array(img)  # 이미지를 NumPy 배열로 변환

    decrypted_img = dess.DES_CBC_decrypt(img_arr, key, round=round)  # 이미지 복호화

    return decrypted_img

try :
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('localhost', 8080))
except :
    print("Waiting for Server...")
    exit()

print('연결에 성공했습니다.')
filename = input('전송할 파일 이름을 입력하세요: ')
clientSock.sendall(filename.encode('utf-8'))
 
# msg = clientSock.recv(1024) 
# if msg:
#     print(msg.decode())



data = clientSock.recv(1024)
data_transferred = 0


nowdir = os.getcwd()
print(nowdir)
while(True):
    # if msg:
    #     filename = 'Encrypted_img.jpg'
    
    select = int(input('1. 파일 받기 \n2. 이미지 복호화\n입력>>'))
    if select == 1:
        if not data:
            print('파일 %s 가 서버에 존재하지 않음' % filename)
            sys.exit()

        
        with open("/Users/pcy/Desktop/무제 폴더/client/" + filename, 'wb') as f: #현재dir에 filename으로 파일을 받는다
            try:
                while data: #데이터가 있을 때까지
                    f.write(data) #1024바이트 쓴다
                    data_transferred += len(data)
                    data = clientSock.recv(1024) #1024바이트를 받아 온다
            except Exception as ex:
                print(ex)
        print('파일 "%s" 받기 완료. 전송량 %d' % (filename, data_transferred))

    
    elif select == 2:
        if not data:
            print('파일 %s 가 서버에 존재하지 않음' % filename)
            sys.exit()

        filename = 'Encrypted_img.jpg'
        with open(nowdir + "/" + filename, 'wb') as f:  # 현재 디렉토리에 파일을 받습니다.
            try:
                while data:  # 데이터가 있을 때까지
                    f.write(data)  # 1024바이트를 씁니다.
                    data_transferred += len(data)
                    data = clientSock.recv(1024)  # 1024바이트를 받아 옵니다.
            except Exception as ex:
                print(ex)
        print('파일 "%s" 받기 완료. 전송량 %d' % (filename, data_transferred))

        print("이미지를 복호화 중...")

        # 이미지 복호화
        decrypted_img = decrypt_image(nowdir + "/" + filename, [1, 2, 3, 4, 5, 6, 7, 8], round=16)

        # 복호화된 이미지 저장
        decrypted_filename = 'Decrypted_img.jpg'
        cv2.imwrite(nowdir + "/" + decrypted_filename, decrypted_img)
        print('암호화된 이미지 복호화 완료. "%s" 이름으로 저장되었습니다.' % decrypted_filename)
    elif select == 3:
        exit()    
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        continue
    
print("파일 전송 끝")
sys.exit()
import socket
import os
from DES import myDES

HOST = 'localhost'
PORT = 8081
nowdir = os.getcwd()


# 서버로부터 파일을 받아오는 함수(파일 이름)
def getFileFromServer(filename):
    data_transferred = 0

    #IP_4 Version으로 TCP방식으로 설정
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT)) # 해당 포트와 호스트로 연결
        sock.sendall(filename.encode()) # 파일이름을 인코딩(바이트화)해서 서버로 보냄

        key = sock.recv(8) # Key는 8byte이므로 8byte만 받아옴
        # ECB모드라면 iv는 필요없으므로 해당 코드 삭제-----------------
        iv = sock.recv(8) # iv도 마찬가지
        data = sock.recv(1024) # 데이터는 1024byte씩 받아오면됨(해당 테스트에선 1줄이어서 한번만)

        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 오류 발생'%filename)
            return

        # 복호화가 제대로 됐는지 확인하기 위해 파일로 저장
        with open(nowdir+"/"+filename,'wb') as f:
            try:
                # 해당 키와 iv로 복호화
                des = myDES(key.decode(),'') # EBC 모드라면 iv쪽을 ''로 비워둠

                # 데이터를 다 읽을때까지 읽어들여 데이터를 복호화
                while data:
                    f.write(des) #1024바이트 쓴다
                    data_transferred += len(data)
                    data = sock.recv(1024) #1024바이트를 받아 온다


            except Exception as e:
                print(e)

            print('파일 [%s] 전송 종료. 전송량 [%d]' %(filename, data_transferred))

getFileFromServer('glogo.png')
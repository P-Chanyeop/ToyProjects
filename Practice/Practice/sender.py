import socketserver
from DES import myDES
from os.path import exists
HOST = ''
PORT = 8081
# 임의의 키와 IV를 만듦
DESKEY = 'eightkey'
DESIV = '1234'

# 들어오는 요청을 처리하는 핸들러 클래스를 재정의한 요청처리기
class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s]연결됨' % self.client_address[0])
        # 1024 바이트 받기
        filename = self.request.recv(1024)
        filename = filename.decode()

        if not exists(filename):
            return

        print('파일 [%s] 전송 시작..' % filename)

        #키와 IV 값을 클라이언트에게 보냄
        self.request.send(DESKEY.encode("utf-8"))
        self.request.send(DESIV.encode("utf-8")) # ECB 모드면 삭제

        with open(filename,'r') as file:
            try:
                line = file.readline()
                des = myDES(DESKEY,DESIV)
                enc = des.encrypt_CBC(line)
                data_transferred += self.request.send(enc)
            except Exception as e:
                print(e)


        print('전송 완료[%s],전송량[%d]' % (filename, data_transferred))

def runServer():
     print('파일 서버 시작')
     try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        # Ctrl + C 하기 전까진 계속 서버 실행
        server.serve_forever()
     except KeyboardInterrupt:
         print('파일 서버 종료')            
runServer()
<<<<<<< HEAD:Practice/simpleLogin.py
# auth 모듈로 애플리케이션 입력 기능 넣기
import auth

input_id = input("아이디를 입력해주세요.\n")
if auth.login(input_id):
    print('Hello, ' + input_id)
else:
    print('Who are you?')
=======
# 애플리케이션 입력 기능 넣기
input_id = input("아이디를 입력해주세요.\n")
# real_egoing = "egoing"
# real_yeop = "yeop"
names = ['egoing', 'yeop']
for name in names:
    if(name == input_id):
        print("Hello! " + name)
        import sys
        sys.exit()      # 파이썬 시스템 종료. 
print("Who are you?")        
>>>>>>> 4295ed5 (create new simple examples by python):Python/simpleLogin.py

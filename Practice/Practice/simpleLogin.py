# auth 모듈로 애플리케이션 입력 기능 넣기
import auth

input_id = input("아이디를 입력해주세요.\n")
if auth.login(input_id):
    print('Hello, ' + input_id)
else:
    print('Who are you?')

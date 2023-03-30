# 문자와 데이터형
print('hello ' + 'world')    # 문자열의 연결
print('hello' * 3)  # 문자열의 반복출력
#print('hello' - 'world')    # Compile Error
print('hello'[0])   # 해당 인덱스번호에 해당하는 문자 출력

# 문자의 제어
print('hello world'.capitalize())   # 첫 문자를 대문자로 변환하여 출력
print('hello world'.upper())    # 모든 문자를 대문자로 변환하여 출력
print('HELLO WORLD'.lower())    # 모든 문자를 소문자로 변환하여 출력
print(len('hello world'))    # 문자열의 길이 출력(공백 포함)
print('hello world'.__len__())    # 문자열의 길이 출력(공백 포함)
print('Hello world'.replace('world', 'programming'))    # 'world'라는 문자열을 'programming'으로 대체하여 출력

# 특수한 문자 케이스
print("egoing's \"tutorial\"")      # 특수 문자를 넣는 방법 \" ... \"
print("\\")     # '\' 특수문자를 넣는 방법 
print("Hello\nworld")       # 줄바꿈 특수문자 \n
print("Hello\tworld")       # 공백을 넣는 특수문자 \t
print("\a")     # 기본 경고음을 소리나게함 \a
print('Hello\nworld')   # 작은따옴표와 큰따옴표가 같은 기능을 함.

# 문자와 숫자를 통한 데이터 타입 차이점
print(10 + 5)       # 15
print("10" + "5")       # 105
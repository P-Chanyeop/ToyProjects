# 변수 예제
x = 10
y = 5
print(x + y)

title = "python"
print("title : " + title)

# 변수의 문법
name = "박찬엽"
print("안녕하세요. " + name + "님")
print(name + "님을 위한 강의")

# 수 계산에서의 변수 사용
donation = 200
student = 10
sponsor = 100
print(int(donation * student / sponsor))

# 애플리케이션 입력 기능 넣기
in_str = input("입력해주세요.\n")
real_id = "11"
real_yeop = "ab"
if (real_id == in_str):
    print("Hello ! yeop")
elif real_yeop == in_str:
    print("Hello ! ab!")
else:
    print("Who are you?")
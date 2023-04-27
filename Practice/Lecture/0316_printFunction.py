# print function variable example
# 파이썬은 인터프리터 언어이기 때문에 한줄씩 실행을 하여 4번째 print까지 수행한 후 다음 print함수를 실행할 때 오류발생.

print("안녕하세요") 
print("%d" % 100)   # 정수 100
print("100 + 100")  # 100100
print("%d" % (100 + 100))   # 정수 200
# print("%d" % (100, 200))    # not all arguments converted during string formatting 에러
# print("%d %d" % 100)    # not enough arguments 에러

# 소숫점 나타내기
print("%d / %d = %5.1f" % (100, 200, 0.5))  # 100 / 200 =     0.5
print("%d / %d = %d" % (100, 200, 0.5)) # 100 / 200 = 0. 0.5를 정수형으로 바꿔버리기 때문에 0이 출력.

# 깔끔한 출력
print("%d" % 123)
print("%5d" % 123)  # [2칸 공백]123 출력
print("%05d" % 123)     # 00123 출력

print("%f" % 123.45)    # 123.450000 출력
print("%7.1f" % 123.45) # [세칸공백]123.5
print("%7.3f" % 123.45) # 123.450 출력

print("%s" % "Python")  # Python 출력
print("%10s" % "Python")    # [네칸공백]Python 출력

print("%d %d %05d" % (123, 123, 123))   # 123 123 00123 출력
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))    # 123 [두칸공백]123 00123 출력

# 다양한 이스케이프 문자 
print("\n 줄바꾸기 연습")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과")
print("글자가 \'강조\'되는 효과")
print("\\\\\\ 역슬래시 세개 출력")
print(r"\n \y \" \\를 그대로 출력")

# 다이아몬드 찍기 프로그램
print("   *   ")
print("  ***  ")
print(" ***** ")
print("  ***  ")
print("   *   ")

# for문 활용
# 다이아몬드 찍기 프로그램
n = int(input('숫자를 입력하세요: '))

# 윗 부분 출력
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 아랫 부분 출력
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

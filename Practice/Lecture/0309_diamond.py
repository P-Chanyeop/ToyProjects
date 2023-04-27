# 다이아몬드 찍기 프로그램
n = int(input('숫자를 입력하세요: '))

# 윗 부분 출력
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 아랫 부분 출력
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
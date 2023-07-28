# 2 차원 튜플의 사용

tt = ((1, 2, 3),
      (4, 5, 6),
      (7, 8, 9))

for i in range(3):
    for j in range(3):
        print(f'{tt[i][j]}   ', end='')
    print()
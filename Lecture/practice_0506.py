# 랜덤하게 1 ~ 20까지 숫자를 20개 채운 후에, 뽑힌 숫자 목록을 추출하는 코드를 작성.
import random

numbers = []    # 빈 리스트 생성
for num in range(0, 20):
    numbers.append(random.randrange(0, 20)+1)
    
print('생성된 리스트', numbers)

for num in range(0, 20):
    if num in numbers:
        print("숫자 %d는(은) 뽑혔습니다." % num)
    
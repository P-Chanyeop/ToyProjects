# 값을 10개를 입력 받아 합계를 출력하도록 07-03 코드를 수정해라. (단, while문 사용)

array = []
i = 0
hap = 0
number = int(input('입력할 원소 갯수 : '))

for _ in range(0, number):
    array.append(0)
    
while i < number:
    array[i] = int(input(f'{i+1}번째 숫자 : '))
    hap += array[i]
    i += 1
    
print(f'합계 : {hap}')
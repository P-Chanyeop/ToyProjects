# for문 예제
# 파이썬의 기본 for문 구조
# for 변수 in 리스트(또는 튜플, 문자열): 수행할 문장

# 전형적인 for문
# one이 처음 i 변수에 대입된후 출력, two가 i에 대입된 후 출력,,,
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)    # one two three 출력
    

# for문의 응용
marks = [90, 25, 67, 45, 80]
number = 0
for i in marks:
    number += 1
    if(i >= 60):
        print(f'{number}번 학생은 합격입니다.')
    else:
        print(f'{number}번 학생은 불합격입니다.')
        
# for 과 range 함수
# for i in range(0, 10). 0부터 10미만의 범위. 10은 포함되지 않는다.
add = 0
for i in range(1, 11):
    add += i
    
print(add)  # 1 ~ 10까지의 합계 출력

number = 0
for i in range(len(marks)):# marks리스트의 길이만큼. 즉 for i in range(0, 5)와 같다. 
    number += 1
    if marks[i] < 60:
        continue    # 다음 루프로 건너뛰기
    print(f'{number}번 학생은 합격입니다.')
    

# 리스트 컨프리헨션 예제
# 리스트 안에 for문을 포함하는 것.

a = [1, 2, 3, 4]
result = []
for i in a:
    result.append(i * 3)
    
print(result)   # [3, 6, 9, 12] 출력

# 위 예제를 리스트 컨프리헨션 수행
result = [i * 3 for i in a]
print(result)   # [3, 6, 9, 12] 출력

# if문을 포함하는 리스트 컨프리헨션
result = [i * 3 for i in a if i % 2 == 0]
print(result)   # [6, 12] 출력. 짝수에만 *3을 하여 담는다

# for문을 2개 이상 사용하는 예제
result = [x * y for x in range(2, 6)
                for y in range(1, 6)]
print(result)   # [2, 4, ..., 20, 25] 출력. 2의 배수 5개, 3의 배수 5개... 중첩 for문과 같다.
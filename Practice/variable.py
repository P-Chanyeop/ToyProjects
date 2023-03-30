# Variable example 
# 변수의 할당(객체생성-> 값을 메모리(저장공간)에 저장 -> 변수는 메모리의 주소를 가리킴)

# 변수 예제(id함수 사용. 가리키고 있는 객체의 주소값을 리턴하는 내장함수)
a = [1, 2, 3]
print(id(a))    # 4310464320(메모리 주소값)

# 변수의 복사
b = a 
print(id(b))    # a의 주소와 같다.

a[1] = 4    # 같은 주소를 가리키고 있기 떄문에 a를 수정하면 b도 같이 수정된다.
print(a, b)     # [1, 4, 3][1, 4, 3]


# 가리키는 주소 변경하기
# [:] 이용. 리스트 전체를 가리키는 도구를 이용하여 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(id(a), id(b))     # 메모리 주소값이 서로 다름(다른 객체)
print(a, b)    # [1, 4, 3][1, 2, 3]. b값이 변경되지 않음

# copy 모듈 이용하기(import copy or list 자체함수 copy 사용)
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(b is a)   # False. 값은 같지만 a와 b는 서로 다른객체를 가리키고 있다.


# 변수를 만드는 다양한 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python'

# Swap 
# 파이썬에서는 위 방법을 사용하여 아주 간단하게 두 변수의 값을 바꿀 수 있다.
a, b = 3, 5
a, b = b, a
print(a, b)     # 5 3 출력
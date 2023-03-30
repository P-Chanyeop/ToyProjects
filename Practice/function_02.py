# Python function example
### 함수의 기본 구조
# def 함수명(매개변수): <수행할 문장>...

# a, b를 매개변수로 받아와 a + b를 반환하는 함수
def add(a, b):
    return a + b

a = 3
b = 4
print(add(a, b))    # 7 출력.


### 매개변수와 인수??
def add(a, b):  # a, b는 매개변수
    return a + b

print(add(3, 4))    # 3, 4는 인수


### 함수의 종류
# 일반적인 함수 예시
def add(a, b):
    result = a + b
    return result

# 입력값이 없는 함수(매개변수가 없는 함수)
def say():
    return 'Hi'
print(say())    # Hi 출력

# 리턴값이 없는 함수 (수행할 문장에 해당하는 수행문만 수행되고 반환값이 없다)
def add(a, b):
    print("%d, %d의 합은 %d입니다" % (a, b, (a + b)))
add(3,4)    # 3, 4의 합은 7입니다. 출력    

# 입력값도 리턴값도 없는 함수
def say():
    print('Hi')
say()   # 'Hi'출력.


### 매개변수 지정하여 호출하기 (매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.)
def sub(a, b):
    return a - b
result = sub(a = 7, b = 3)  
result = sub(b = 3, a = 7)


### 여러개의 입력값을 받는 함수 만들기(매개변수의 개수가 변화가능성이 있음)
# Python에서는 *매개변수를 통해 입력값이 몇개든 상관없이 함수로 만들 수 있다.
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5))  # 15 출력.

# 여러개의 입력값을 받는 함수 응용
def add_mul(choice, *args):
    if(choice == 'add'):
        result = 0
        for i in args:
            result += i
    elif (choice == 'mul'):
        result = 1
        for i in args:
            result *= i
    return result
print(add_mul('add', 1, 2, 3, 4))  # 10 출력.
print(add_mul('mul', 1, 2, 3, 4))   # 24 출력

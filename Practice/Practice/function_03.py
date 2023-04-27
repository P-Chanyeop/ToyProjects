## Python function example 03

# 키워드 매개변수 kwargs 예제
# 입력값과 변수를 이용하여 딕셔너리로 반환{key : value}
def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a = 1)     # {'a' : 1} 출력.
print_kwargs(name = 'foo', age = 3) # {'age' : 3 , 'name' : 'foo'} 출력


## 함수의 리턴값은 항상 하나
# 리턴할 것이 여러개면 하나로 묶어 튜플로 반환이된다 
def add_and_mul(a, b):
    return a + b, a * b

print(add_and_mul(3, 4))  # (7, 12) 출력

# 리턴값을 튜플이 안닌 하나씩 받고싶다면
result1, result2 = add_and_mul(3, 4)
print(result1, result2) # 7 12 출력

# 리턴이 여러개라면? 첫번째 리턴문을 만나면 함수를 빠져나온다
def add_and_mul(a, b):
    return a + b
    return a * b    # 실행되지 않음


## 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나의 나이는 %d 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself("박찬엽", 27)    # 기본값으로 man = True의 값을 갖게된다.
say_myself("박순", 27, False)   # False값을 매개변수로 넣어줄 수도 있다.

# 초기값을 미리 설정하려면 뒤에 놓아야한다
# 다음 함수는 non-defualt argument follows default argument 에러를 발생시킨다.
# def say_myself1(name, man=True, age):...
        
        
## 함수 안에서 선언한 변수의 효력 범위 
# 함수안에서 선언한 변수의 경우 지역변수이기 떄문에 함수가 종료되면 변수가 사라짐. 밖에서 사용불가

# 함수안에서 밖에 있는 변수를 변화시키기
# 1. 리턴문 사용
a= 1
def vartest(a):
    a += 1
    return a
a = vartest(a)
print(a)    # 2 출력

# 2. global 명령어 사용
# 함수밖의 변수를 직접 사용하겠다는 의미. 함수는 독립적으로 외부 변수에 종속적이지 않게 만드는게 좋다. 가급적 global 명령어를 사용하지 않는게 좋다.
a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)    # 2 출력 


## Lambda 함수 
# 함수를 생성할때 사용하는 예약어, def와 같은 역할. 함수를 한줄로 간결하게 만들때 사용한다.
# 함수명 = lambda 매개변수1,... : 매개변수를 이용한 표현식

add = lambda a, b: a + b
print(add(3, 4))    # 7 출력

# 위 람다 함수와 같다.
def add1(a, b):
    return a + b

print(add1(3, 4))    # 7 출력
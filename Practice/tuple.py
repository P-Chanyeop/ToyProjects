### tuple example
# 튜플의 요소값은 삭제와 수정, 추가가(변화) 불가능하다.

#### 튜플 생성 형식###
t1 = () 
t2 = (1,)    # 요소가 하나일 때에는 뒤에 , 를 붙여준다.
t3 = (1, 2, 3)
t4 = 1, 2, 3    # () 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))


### 튜플값을 변화 할때 ###
# del t3[1]    tuple object doesn't support item deletion 오류
# t1[0] = 'c'   tuple' object does not support item assignment 오류


### 튜플 다루기 ###
# 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])

# 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[1:])

# 튜플 더하기
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)      # t1, t2의 기존 튜플의 요소값이 바뀌는게 아닌 새로운 튜플을 생성 한것.

# 튜플 곱하기
t2 = (3, 4)
print(t2 * 3)   # t2 튜플의 반복

# 튜플의 길이 구하기
t1 = (1, 2, 'a', 'b')
print(len(t1))      

### result ###
# 튜플은 리스트왜 매우 유사하지만, 
# 요소값을 변경할 수 없다는 특징이 있기 때문에, pop, insert, remove, sort 와 같은 내장 함수를 사용할 수 없다.
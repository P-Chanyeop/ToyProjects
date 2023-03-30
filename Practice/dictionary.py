# Dictionary Datatype in Python
# Java의 Map 자료형과 비슷하다
# key와 value로 이루어진 연관배열, 또는 해시 라고 한다
# 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 key를 통해 value를 얻는 것이 가장 큰 특징이다.


# Dictionary 생성
dic = {'name':'park', 'phone':'010-1111-2222', 'birth':'1997'}  # 기본 Dictionary 타입 형태

a = {'a':[1, 2, 3]}     # Dictionary에는 Value값으로 리스트도 추가가 가능하다.


# Dictionary 쌍 추가하기    name['key'] = 'value'
a = {1:'a'}
a[2] = 'b'  # key를 2로, value를 'b'로 하여 추가
a['name'] = 'park'    # key를 'name'으로, value를 'park'으로 하여 추가도 가능
print(a)


# Dictionary 요소 삭제하기  del name['key']
del a[1]    # key값이 1인 요소를 삭제한다.  
print(a)


# Dictionary 사용하기
grade = {'park': 10, 'lee': 99}
print(grade['park'])    # 10. value값이 출력된다.

a = {1:'a', 2:'b'}
print(a[1])     # 'b'. 역시 value값이 출력된다.


### Dictionary 주의 사항!! ###
# key는 고유한 값이므로 동일한 key값이 잇는경우, 하나를 제외한 나머지 key값들은 모두 무시된다.
# Dictionary의 키로 쓸수 있는지에 대한 것은 변하는(mutable)값인지 변하지 않는(immutable)값인지에 달려있다.
# 튜플은 요소를 변화시킬 수 없기때문에 key로 사용이 가능하며, 리스트는 그 값이 변할 수 있기 떄문에 key로 쓸 수 없다.

# key의 중복 문제 예시
a = {1:'a', 1:'b'}
print(a)    # {1: 'b'} 만 출력이 된다. 

# 튜플 key 사용 예시
a = {(1,2,3) : 'a'}
print(a)

# 리스트 key 사용 예시
# a = {[1,2,3] : 'a'}     # TypeError: unhashable type: 'list' 에러 
# print(a)


# Key 리스트 만들기
# dic의 key를 모아서 dict_keys객체를 리턴한다
# dict_keys, dict_values, dict_items 객체는 리스트로 변환하지 않더라도 기본적인 반복구문에 사용이 가능하다.
# 하지만 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
dic = {'name':'park', 'phone':'010-1111-2222', 'birth':'1997'}  # 기본 Dictionary 타입 형태
print(list(dic.keys()))  # dict_keys객체가 아닌 리스트로 리턴값을 반환하는 방법

# dict_keys를 이용한 반복 구문
for k in dic.keys():
    print(k)
    
# value 리스트 만들기 (key와 유사)
print(dic.values())     # dict_values 객체를 반환한다.

# key와 value 쌍 얻기(item)
print(dic.items())    # dict_items 객체를 리턴한다.


# key:value 쌍 모두 지우기(clear)
# 딕셔너리 안의 모든 요소를 삭제한다.
dic.clear()
print(dic)      # {} 빈 딕셔너리 출력


# key 로 value 얻기(get)
# dic['name']을 사용했을때와 결과는 같다. 
# 존재하지 않는 키를 가져올 경우 dic['name']타입은 오류를 발생시키고, dic.get('name')방식은 None을 반환한다.
dic = {'name':'park', 'phone':'010-1111-2222', 'birth':'1997'}  # 기본 Dictionary 타입 형태
print(dic.get('name'))  # park 출력

# print(dic['a'])     # KeyError 발생
print(dic.get('a'))     # None 출력. "거짓" 이라는 뜻이다.
print(dic.get('a', 'default'))      # key가 없을 때 default값을 대신 가져올 수 있다.

# 해당 key가 딕셔너리에 있는지 조사(in)
print('name' in dic)    # True
print('a' in dic)   # False
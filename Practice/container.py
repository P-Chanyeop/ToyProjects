# 컨테이너 기본 문법 예제 (파이썬에서의 List,,,etc)
# 변수 : 하나의 값을 담는 그릇. 컨테이너를 활용하여 여러개를 담을 수 있다.
name = ['egoing', 'leezche', 'graphittie']
print(type(name))   # <class 'list'>
print(name)     # ['egoing', 'leezche', 'graphittie']
print(name[2])  # graphittie . 인덱스를 통해 리스트에 접근 가능

egoing = ['programmer', 'seoul', 25, False]
egoing[1] = 'busan'     # 인덱스를 통해 리스트의 내용을 바꿀 수 있음.
egoing.append('hi')     # .append를 통해 리스트의 원소를 추가 가능
egoing.remove('hi')     # .remove를 통해 리스트의 원소를 삭제
print(egoing)   # ['programmer', 'busan', 25, False]

# 리스트 심화
a1 = ['a','b','c','d']
print(len(a1))
a1.append('e')      # 마지막 위치에 원소 추가
print(a1)
del(a1[0])      # 해당 인덱스의 원소 삭제
print(a1)

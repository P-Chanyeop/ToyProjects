# set 자료형 예시
# 자바의 HashSet자료형과 유사하다. 
# 중복을 허용하지 않으며, 순서가 없다.

# set 자료형의 생성
s1 = set([1,2,3])
print(s1)

s1 = set("Hello")
print(s1)   # 중복을 허용하지 않아 helo가 출력된다.


# 교집합 구하기(&)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)  # {4, 5, 6} 출력
print(s1.intersection(s2))     # 결과는 동일

# 합집합 구하기(|)
print(s1 | s2)  # {1, 2, 3, ... , 8, 9}
print(s1.union(s2))

#차집합 구하기(-)
print(s1 - s2)  # {1, 2, 3} 출력
print(s1.difference(s2))



# set 집합 자료형 관련 함수들
# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)   # {1, 2, 3, 4} 출력

# 값 여러개 추가하기(update)
s1.update([5, 6, 7])    # {1, 2, ... , 6, 7} 출력
print(s1)

# 특정 값 추가하기(remove)
s1.remove(1)    # {2, 3, ... , 6, 7} 출력
print(s1)
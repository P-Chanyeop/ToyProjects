# 리스트의 사용
# 생성 : 리스트명 = [요소1, 요소2, 요소3, ...]

# 인덱싱 
a = [1, 2, 3]
print(a)    # [1, 2, 3]
print(a[0])     # 1. 리스트의 첫 번째 요소 값 출력
print(a[0] + a[2])      # 4. 리스트의 첫 번째, 세 번째 요소 값을 더한값 출력

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1])   # ['a', 'b', 'c']. 리스트의 마지막 요소 출력
print(a[3])     # ['a', 'b', 'c']. 리스트의 네 번쨰 요소 출력
print(a[-1][0])     # a. a리스트의 마지막 요소의 첫 번쨰 요소 출력
print(a[-1][1])     # b. a리스트의 마지막 요소의 두 번쨰 요소 출력
print(a[-1][2])     # c. a리스트의 마지막 요소의 세 번쨰 요소 출력

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])      # [1, 2]. a리스트의 첫번째 요소부터 2번째 요소까지 잘라서 출력. 여기서 세 번째(a[2])요소는 출력되지 않는다.

b = a[:2]
print(b)    # [1, 2]. a[0:2]와 결과가 같다.

c = a[2:] 
print(c)    # [3, 4, 5]. a리스트의 세 번쨰요소(a[2]) 부터 마지막 요소까지 출력 

# 리스트 연산하기

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)    # [1, 2, 3, 4, 5, 6]. 문자열의 "abc" + "def" 와 같은 이치이다. 두 리스트를 합친 결과 출력.

# 리스트 반복하기
a = [1, 2, 3]  
print(a * 3)    # [1, 2, 3, 1, 2, 3, ...]. "abc" * 3 = "abcabcabc"와 같은 이치이다. 리스트를 세번 반복한 결과 출력.

# 리스트의 길이 
a = [1, 2, 3]
print(len(a))   # 3. a리스트의 길이를 구한다.

# 실수 주의
a = [1, 2, 3]
#print(a[2] + "hi")  # TypeError. 3 + hi 를 3hi라고 착각하기 쉬움. a[2]는 int형, hi는 str형이기 때문에 형 오류 발생.

# 리스트의 수정과 삭제 
a = [1, 2, 3]
a[2] = 4    # a[2]값(3) 을 4로 변경
print(a[2])     # 4 출력

# del를 이용하여 리스트 요소 삭제. ( del 객체 ) 객체란 파이썬에서 사용되는 모든 자료형
a = [1, 2, 3]
del a[1]    # a[1]요소 삭제
print(a)    # [1, 3] 출력.

a = [1, 2, 3, 4, 5]
del a[2:]   # a리스트의 세번째 요소부터 마지막 요소까지 모두 삭제. 슬라이싱 기법을 활용한 삭제
print(a)    # [1, 2] 출력.

# 리스트 관련 함수들
# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)     # a리스트의 마지막에 4 추가
print(a)    # [1, 2, 3, 4] 출력.

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()    # a리스트을 순서대로 정렬. 알파벳도 가능하다. 단, 서로 섞여있으면 오류
print(a)    # [1, 2, 3, 4] 출력.

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()     # a리스트를 뒤집어 출력.
print(a)    # ['b', 'c', 'a'] 츌력.

# 인덱스 반환
a = [1, 2, 3]
print(a.index(3))      # 2. 값 3의 인덱스 번호 출력
print(a.index(1))       # 0. 값 1의 인덱스 번호 출력. 값이 리스트에 존재하지 않는 경우 ValueError 발생.

# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)      # a[0] 위치에 4 삽입.
print(a)      # [4, 1, 2, 3] 출력.

a.insert(3, 5)      # a[3] 위치에 5 삽입
print(a)    # [4, 1, 2, 5, 3] 출력

# 리스트의 요소 제거(remove). 리스트에서 첫 번째로 나오는 요소를 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)     # 첫 번째로 나오는 3 삭제
print(a)    # [1, 2, 1, 2, 3] 출력.

# 리스트의 요소 꺼내기(pop). 리스트의 맨 마지막 요소를 리턴하고 그 요소를 삭제
a = [1, 2, 3]
a.pop()     # 맨 마지막 요소 리턴 후 삭제
print(a)    # [1, 2] 출력

# 리스트에 포함된 요소 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))  # 2 출력. 값 1의 개수 세기

# 리스트 확장(extend). 인자로 리스트만 올 수 있다. a리스트에 인자로 온 리스트를 더한다.
a = [1, 2, 3]
a.extend([4,5])     # a리스트에 [4,5]리스트를 더한다. a += [4,5] 와 동일
print(a)     # [1, 2, 3, 4, 5] 출력.


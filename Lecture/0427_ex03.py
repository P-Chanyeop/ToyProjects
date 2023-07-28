# 07-05 코드 작성

# 리스트 초기화 및 현재리스트 확인
myList = [30, 10, 20]
print(f'현재 리스트 : {myList}')

# 리스트에 40 추가 
myList.append(40)
print(f'40 append 후 리스트 : {myList}')

# 리스트의 마지막 요소 추출. 삭제 O
print(f'pop()으로 추출한 값 : {myList.pop()}')
print(f'pop() 후의 리스트 : {myList}')

# 리스트 오름차순 정렬
myList.sort()
print(f'sort() 이후의 리스트 : {myList}')

# 리스트를 역순으로 정렬
myList.reverse()
print(f'reverse() 이후의 리스트 : {myList}')

# 20의 인덱스 번호 출력
print(f'20의 위치 : {myList.index(20)}')

# 리스트의 index번호 위치에 데이터 삽입. 그 위치에 있던 요소는 뒤로 밀려남
myList.insert(2, 222)
print(f'insert(2, 222) 이후의 리스트 : {myList}')

# 리스트에 있는 (222) 요소 삭제 
myList.remove(222)
print(f'remove(222) 이후의 리스트 : {myList}')

# 리스트 확장. 뒤에 77, 88, 77 요소를 덧 붙임
myList.extend([77, 88, 77])
print(f'extend([77, 88, 77] 이후의 리스트 : {myList}')

# 리스트안의 77의 요소 개수 출력
print(f'77의 개수 : {myList.count(77)}')

# 리스트의 정렬
print(f'sorted()된 리스트 : {sorted(myList)}')


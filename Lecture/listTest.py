# 리스트, 튜플, 딕셔너리 테스트
a = [1,2,3]
b = [4,5,6]

# 리스트 끼리의 덧셈은 리스트를 합침
print(a+b)

# 리스트의 곱은 리스트를 반복
print(a*3)

# 리스트 조작
a.append(4)
b.pop(0)    # 인덱스로 접근하여 삭제

print(a,b)

a = [4,1,3]
a.sort()
print(a)
a.index(1)
print(a.index(4))   # 해당 원소가 있는 인덱스 반환

# 튜플은 값을 수정할 수 없으며, 읽기만 가능
t = (1, 2, 3)
t2 = 1,2,1

print(t, t2[1])

# 딕셔너리는 키와 값 쌍으로 이루어진 자료형
dic = {"apple": "사과", "hello":"안녕"}
print(dic.get("apple"))
print(dic["apple"])     # 출력

dic["player"] = "선수"  # 삽입
print(dic)

del dic["player"] # 삭제
print(dic)

print(dic.keys())   # 키 출력
print(dic.values()) # 값 출력

print("안녕", 1234, '하세요')
print(3.14, 'ㅋ', 500)

a = [[6,7,8,9],
    [1,2,3,4]]
print(a[1])

b = ((1,2), (3,4))
print(b[1])

ss = 'IT_CookBook_Python'
outStr = ''

for i in range(0, len(ss)):
    if i % 2 == 0:
        outStr += ss[-i-1]
    else:
        outStr += '#'
        
print(ss)
print(outStr)

ss = 'Python'
for i in range(0, len(ss)):
    print(ss[-i-1])
    
ss = 'python ### CookBook $$$ @@@ study 1234'
for i in ss:
    if not i.isalpha():
        ss = ss.replace(i,'')
print(ss)
ss.isupper()

대문자 =''
소문자 =''
숫자 = ''
한글 = ''
기타 = ''
inStr = 'IT CookBook 파이썬을 365일 공부하고 있습니다. ^___^'

for i in range(len(inStr)):
    if inStr[i].isupper() and (65 <= ord(inStr[i]) <= 90):
        대문자 += inStr[i]
    elif inStr[i].islower() and (97 <= ord(inStr[i]) <= 122):
        소문자 += inStr[i]
    elif inStr[i].isdigit():
        숫자 += inStr[i]
    elif inStr[i].isalpha():
        한글 += inStr[i]
    else:
        기타 += inStr[i]
print(대문자 + "\n", 소문자 + "\n", 숫자 + "\n", 한글 + "\n", 기타)

# 새로운 파일 생성
f = open("새파일.txt", 'w')
f.close()

# 파일 내용 쓰기
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d줄 입니다\n" % i
    f.write(data)
f.close()

# 파일 내용 읽기
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("새파일.txt", 'r')
for line in f:
    print(line)
f.close()

# 파일에 내용 추가하기
f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d줄 입니다.\n" % i
    f.write(data)
f.close()

# 파일 자동으로 열고 닫기
with open("새파일.txt", 'w') as f:
    f.write("Life is too short")
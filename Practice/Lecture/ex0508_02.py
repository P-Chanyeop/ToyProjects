jumsu = 55
res = ''
if jumsu >=60:
    res = '합격'
else :
    res = '불합격' 

print(res)


## 위 if문을 삼항연산자로 변환
res = '합격' if jumsu >= 60 else '불합격'
print(res)
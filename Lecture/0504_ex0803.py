## 문자열 함수 예제

s = "im SICK now.... HELP me plz"

# 1. upper()함수 - 모든 문자를 대문자로 변환
print(s.upper())

# 2. lower()함수 - 모든 문자를 소문자로 변환
print(s.lower())

# 3. swapcase()함수 - 대문자는 소문자로, 소문자는 대문자로 변환
print(s.swapcase())

# 4. title()함수 - 단어의 맨 앞 문자를 대문자로 설정
print(s.title())

# 5. count('문자열')함수 - '문자열'에 해당하는 것이 포함된 개수 반환
print(s.count('m'))

# 6. find('문자열', index)함수 - '문자열'에 해당하는 것이 index 부터 처음으로 나타나는 index 반환. 찾는것이 없으면 -1반환
print(s.find('m'))
print(s.find('m', 2))
print(s.find('play'))

# 7. rfind('문자열')함수 - '문자열'에 해당하는 것이 뒤에서 부터 처음으로 나타나는 index 반환
print(s.rfind('m'))

# 8. index('문자열', index)함수 - '문자열'에 해당하는 것이 index 부터 처음으로 나타나는 index반환. 찾는것이 없다면 오류발생 
print(s.index('m'))
print(s.index('m', 2))
# print(s.index('play'))  - error

# 9. rindex('문자열') - '문자열'에 해당하는 것이 뒤에서 부터 처음으로 나타나는 index 반환
print(s.rindex('m'))

# 10. startswith('문자열', index) - index부터의 문자열이 인자로 주어진 '문자열'로 시작하면 True, 그렇지 않다면 False를 반환
print(s.startswith('im'))
print(s.startswith('SICK', 3))

# 11. endswith('문자열') - 문자열이 해당 '문자열'로 끝나면 True, 그렇지 않으면 False를 반환
print(s.endswith('plz'))

s = ' 파 이 썬 '
# 12. strip()함수 - 문자열 앞 뒤의 공백을 제거
print(s.strip())

# 13. rstrip()함수 - 문자열 뒤의 공백을 제거
print(s.rstrip())

# 14. lstrip()함수 - 문자열 앞의 공백을 제거
print(s.lstrip())

# 15. split()함수 - 문자열을 공백이나 다른 문자로 분리해 리스트 반환
print(s.split())

s = '파\n이\n썬'
# 16. splitlines()함수 - 문자열을 \n 줄 단위로 분리하여 리스트 반환
print(s.splitlines())

s = '%'
# 17. join()함수 - 두개의 문자열을 합쳐준다.
print(s.join("파이썬"))

s = '파이썬'
# 18. center(숫자)함수 - 숫자만큼 전체 자리수를 잡은후 문자열을 가운데 정렬
print(s.center(10))

# 19. center(숫자, '문자')함수 - 숫자만큼 전체 자리수를 잡은후 문자열을 가운데 정렬이후 앞 뒤 빈공간을 '문자'로 채워넣는다.
print(s.center(10, '-'))

# 20. ljust()함수 - 문자열을 왼쪽에 붙여서 출력
print(s.ljust(10))

# 21. rjust()함수 - 문자열을 오른쪽에 붙여서 출력
print(s.rjust(10))

# 22. zfill()함수 - 문자열을 오른쪽으로 붙여서 쓰고 빈공간에는 0으로 채워넣는다
print(s.zfill(10))

# 23. isdigit()함수 - 문자열이 숫자로만 구성되어 있으면 True, 그렇지 않다면 False 반환
print(s.isdigit())

# 24. isalpha()함수 - 문자열이 문자(한글,영어)로만 구성되어 있으면 True, 그렇지 않다면 False 반환
print(s.isalpha())

# 25. isalnum()함수 - 문자열이 문자나 숫자로 구성되어 있으면 True, 그렇지 않다면 False 반환
print(s.isalnum())

# 26. islower()함수 - 문자열 전체가 소문자로 이루어져 있으면 True, 그렇지 않다면 False 반환
print('abcd'.islower())

# 27. isupper()함수 - 문자열 전체가 대문자로 이루어져 있으면 True, 그렇지 않다면 False 반환
print('ABCD'.isupper())

# 28. isspace()함수 - 문자열 전체가 공백으로 이루어져 있으면 True, 그렇지 않다면 False 반환
print('     '.isspace())

# 29. map(함수명, 리스트명)함수 - 리스트값 하나하나를 함수명에 대입한다.
before = ['2019', '12', '31']
after = list(map(int, before))
print(after)
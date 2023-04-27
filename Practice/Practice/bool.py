# bool datatype 
# True or False 를 나타내는 자료형

# 자료형의 참과 거짓 구분 예시
# 자료형의 참과 거짓은 자료형이 비엇으면 False, 그렇지 않으면 True가 된다.
print(bool("python"))   # True
print(bool(""))    # False
print(bool([1,2,3]))    # True
print(bool([]))   # False
print(bool(None))   # False. None은 거짓을 뜻한다는것으로 알아두자.


# 자료형의 참과 거짓 사용 예시
# a가 비어있는 상태가 될때까지 pop을 수행
a = [1, 2, 3, 4]
while a:
    print(a.pop())      # 4,3,2,1 출력. 
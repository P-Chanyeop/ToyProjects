## 함수선언 부분 ##
def calc(v1, v2, op):
    result = 0
    i = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2
    elif op == '**':
        result = 1
        for i in range (v2):
            result *= v1
    
    
    return result


## 전역 변수 선언 부분 ##
res = 0
var1, var2, oper = 0, 0, ""


## 메인 코드 부분 ##
var1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요 (+, -, *, /, **) : ")    
var2 = int(input("두 번째 수를 입력하세요 : "))
if oper == "/" and var2 == 0:
    print("0으로는 나누면 안돼요 ㅠㅠ..")
    exit(0)

res = calc(var1, var2, oper)

print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))
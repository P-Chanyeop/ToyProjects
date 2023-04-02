import random as rd

num1, num2, num3, num4 = rd.randrange(1, 7), rd.randrange(1, 7), rd.randrange(1, 7), rd.randrange(1, 7)

print(f'A의 주사위는 {num1} {num2} 입니다.') 
print(f'B의 주사위는 {num3} {num4} 입니다.')

if (num1 + num2) > (num3 + num4):
    print("A가 이겼습니다.")
elif (num1 + num2) == (num3 + num4):
    print("비겼습니다.")
else:
    print("B가 이겼습니다.")
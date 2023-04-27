# 4행 5열의 리스트를 만들고 0 부터 3의 배수를 입력 받도록 한다.

array1 = []
array2 = []

number = 0
for i in range(4):
    for j in range(5):
        array1.append(number)
        number += 3
    array2.append(array1)
    array1 = []
        
for i in range(4):
    for j in range(5):
        print('%3d' % array2[i][j], end='')
    print()
    

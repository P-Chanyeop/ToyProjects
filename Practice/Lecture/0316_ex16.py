# 진수 판별 프로그램

bin_num = ['0', '1']
oct_num = ['0', '1', '2', '3', '4', '5', '6', '7']
normal_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "A", "B", "C", "D", "E", "F"]

while(1):
    print('')
    num = input("글자 입력>>")
    if(num == 'A' or num == 'B' or num == 'C' or num == 'D' or num == 'E' or num =='F'):
        print("16진수 입니다.")
        break
    if(int(num) >= 0 and int(num) <= 1):
        print("2진수 또는 8진수 또는 16진수 입니다.")
        break
    elif(2 <= int(num) and int(num) <= 7):
        print("8진수 또는 10진수 또는 16진수입니다.")
        break
    elif(7 < int(num) and int(num) <= 9):
        print("10진수 또는 16진수 입니다.")
        break
    else:
        print("입력 오류!!")
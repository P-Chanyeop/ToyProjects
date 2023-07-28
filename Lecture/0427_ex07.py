# 7-5 동물의 어미와 새끼의 이름을 딕셔너리로 생성

dic = {
    '닭' : '병아리',
    '개' : '강아지',
    '곰' : '능소니',
    '고등어' : '고도리',
    '명태' : '노가리',
    '말' : '망아지',
    '호랑이' : '개호주'
   }

while(True):
    a = input(str(list(dic.keys())) + "중 새끼 이름을 알고 싶은 동물은 ? ")
    if a in dic.keys():
        print(f'{dic.get(a)}')
    elif a == '끝':
        break
    else: print("딕셔너리에 포함되지 않은 동물입니다!")
    
    


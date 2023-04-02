import turtle as tt

## 전역 변수 선언 부분 ##
swidth, sheight = 500, 500

## 메인 코드 부분 ##
if __name__ == '__main__':
    tt.title('무지개색 원그리기')
    tt.shape('turtle')
    tt.setup(width = swidth + 50, height = sheight + 50)
    tt.screensize(swidth, sheight)
    tt.penup()
    tt.goto(0, -sheight / 2)
    tt.pendown()
    tt.speed(0)
    
    count = 0
    
    for radius in range(1, 250):
        if radius % 7 == 1:
            tt.pencolor('red')
        elif radius % 7 == 2:
            tt.pencolor('orange')
        elif radius % 7 == 2:
            tt.pencolor('yellow')
        elif radius % 7 == 3:
            tt.pencolor('green')
        elif radius % 7 == 4:
            tt.pencolor('blue')
        elif radius % 7 == 5:
            tt.pencolor('navyblue')
        else:
            tt.pencolor('purple')
        count += 1
        tt.circle(radius)
    
    print(count)
    tt.done()
    
    
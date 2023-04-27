import turtle
import random

## 함수 선언 부분 ##
def screenRightClick(x, y):
    global r, g, b
    # 랜덤 색상
    r = random.random()
    g = random.random()
    b = random.random()
    
    # 랜덤 크기
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    
    # 랜덤 각도
    tRight = random.randrange(1, 360)
    turtle.right(tRight)
    
    # 거북이 그리기(펜색상, 거북이 색상, 이동, 도장찍기 기능)
    turtle.pencolor((r,g,b))
    turtle.color((r,g,b))
    turtle.pendown()
    turtle.goto(x, y)
    turtle.stamp()
    
## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title("거북이 그리기")
turtle.shape("turtle")
turtle.pensize(pSize)

turtle.onscreenclick(screenRightClick, 2)

turtle.done()
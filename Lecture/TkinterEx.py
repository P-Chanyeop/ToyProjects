import pygame as pg
import random

size = [600, 750]
screen = pg.display.set_mode(size)

pg.display.set_caption("Tetris")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

done = False
clock = pg.time.Clock() 
index = 0
x = -50
y = 0

board = [
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,1,
            1,1,1,1,1,1,1,1,1,1,1,1,
            ]

blocks = [
            
            [
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,
            ],
            [
            0, 0, 0,
            0, 0, 0,
            1, 1, 1,
            ],
            
        
            [
            1, 1, 0,
            1, 0, 0,
            1, 0, 0,
            ]
            ,
            [
            0, 0, 0,
            1, 1, 1,
            0, 0, 1
            ]
            ,
            [
            0, 0, 1,
            0, 0, 1,
            0, 1, 1,
            ],
            

            
            [
            0, 1, 1,
            0, 0, 1,
            0, 0, 1
            ]
            ,
            [
            0, 0, 0,
            0, 0, 1,
            1, 1, 1]
            ,
            [
            1, 0, 0,
            1, 0, 0,
            1, 1, 0,
            ],
            

            
            [
            1, 0, 0,
            1, 1, 0,
            0, 1, 0
            ]
            ,
            [
            0, 0, 0,
            0, 1, 1,
            1, 1, 0,
            ],
            

            
            [
            0, 1, 0,
            1, 1, 0,
            1, 0, 0,
            ]
            ,
            [
            0, 0, 0,
            1, 1, 0,
            0, 1, 1,
            ],
        
            
            [
            0, 0, 0,
            1, 1, 0,
            1, 1, 0,
            ],
            

            
            [
            0, 0, 0,
            0, 1, 0,
            1, 1, 1
            ]
            ,
            [
            1, 0, 0,
            1, 1, 0,
            1, 0, 0,
            ]
            ,
            [
            0, 1, 0,
            1, 1, 0,
            0, 1, 0,
            ]
        ]     



def wall():
    x = -50
    y = 0
    idx = 0
    for i in board:
        x += 50
        idx += 1
        if i == 1:
            pg.draw.rect(screen, GREEN, (x, y, 50, 50),1)
        else:
            continue
        
        if idx % 12 == 0:
            x = -50
            y += 50


# 블럭 랜덤 생성            
def makeBlock():
    block = blocks[random.randint(0, len(blocks)-1)]
    
    return block

# 블럭 화면에 그리기 구현
def moveBlock(block):
    x = 100
    y = 100
    for i in range(len(block)):
        
        x += 50
        if block[i] == 1:
            pg.draw.rect(screen, GREEN, (x, y, 50, 50))
        if i == 2 or i == 5 or i == 8:
            x = 0
            y += 50

# 충돌 감지
def conflict():
    pass

# 줄이 채워지면 사라짐 구현
def lineClear():
    pass

# GameOver 구현
def gameOver():
    pass

# 점수 구현
def score():
    pass

while not done :
    clock.tick(2)
    #vvvvvvv 메인 이벤트 루프vvvvvvv#
    
    # 스크린 초기화
    screen.fill((0,0,0))

    # 벽그리기 
    wall()
    
    # 블록그리기 
    moveBlock(makeBlock())
    y += 10
    
    #이벤트 검사 for 문
    for event in pg.event.get():
        if event.type == pg.KEYDOWN: # If user release what he pressed.
            if event.key == pg.K_LEFT:
                x -= 50
            elif event.key == pg.K_RIGHT:
                x += 50
        if event.type == pg.QUIT: # 창이 닫히는 이벤트가 발생하였는지
           done = True
        
        if event.type == pg.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                to_x = 0
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                to_y = 0

       
            
    pg.display.flip()

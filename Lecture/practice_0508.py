import turtle
import math
import random

t1, t2, t3 = [None] * 3
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6
swidth, sheight = 200, 200

if __name__== "__main__" :
    turtle.title('turtle meeting')
    turtle.setup(width = swidth+50, height = sheight+50)
    turtle.screensize(swidth, sheight)
    
    t1 = turtle.Turtle('turtle'); t1.color('red'); t1.penup()
    t2 = turtle.Turtle('turtle'); t2.color('green'); t2.penup()
    t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.penup()
    
    t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)
    
    while True :
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t1.left(angle); t1.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t2.left(angle); t2.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t3.left(angle); t3.forward(dist)
        
        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()
        
        if math.sqrt(((t1X - t2X) * (t1X - t2X)) + ((t1Y - t2Y) * (t1Y - t2Y))) <= 20 or \
            math.sqrt(((t1X - t3X) * (t1X - t3X)) + ((t1Y - t3Y) * (t1Y - t3Y))) <= 20 or \
            math.sqrt(((t2X - t3X) * (t2X - t3X)) + ((t2Y - t3Y) * (t2Y - t3Y))) <= 20 : 
            t1.turtlesize(random.randrange(1, 5)); t2.turtlesize(random.randrange(1, 5)); t3.turtlesize(random.randrange(1, 5))   
            
        if  -200 > t1X or t1X > 200:
            t1.goto(0, 0)
        elif -200 > t1Y or t1Y > 200:
            t1.goto(0, 0)
            
        if -200 > t2X or t2X > 200:
            t2.goto(0, 0)
        elif -200 > t2Y or t2Y > 200:
            t2.goto(0, 0)
            
        if -200 > t3X or t3X > 200:
            t3.goto(0, 0)
        elif -200 > t3Y or t3Y > 200:
            t3.goto(0, 0)
                
turtle.done()
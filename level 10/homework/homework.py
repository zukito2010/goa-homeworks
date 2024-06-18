from turtle import *

# 5)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.pensize(5)
t2.pensize(5)
t3.pensize(5)


for i in range(4):
    t1.forward(100)
    t1.left(90)


t1.speed(10)
t2.speed(10)
t3.speed(10)



t2.penup()
t2.goto(300,300)
t2.pendown()
t2.color("yellow")
for i in range(30):
    t2.forward(100)
    t2.left(162)


    
length = 0
t3.color("green")
t3.penup()
t3.goto(0,150)
t3.pendown()



for i in range(5):
    length -= 30
    t3.circle(100)
    t3.penup()
    t3.goto(length, 150)
    t3.pendown()        



exitonclick()    
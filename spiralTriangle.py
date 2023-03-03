import turtle
dist = 1
flag = 1500
spiral = turtle.Turtle(
)
turtle.tracer(0)
while flag:
    spiral.forward(dist)
    spiral.left(120)
    spiral.left(1)
    dist+=1
    flag-=1
    turtle.update()
turtle.done()
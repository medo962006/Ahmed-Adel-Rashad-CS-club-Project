import turtle
import random
spiral = turtle.Turtle()
colours = ["red", "blue", "black","green","orange"]
turtle.tracer(0)

for i in range(1000):
    spiral.color(random.choice(colours))  
    spiral.forward(i)
    spiral.right(144)
    turtle.update()
turtle.done()
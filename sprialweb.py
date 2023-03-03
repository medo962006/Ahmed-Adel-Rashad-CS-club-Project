import turtle
colors=['red','yellow','green','blue','purple','orange']
t = turtle.Pen()
turtle.bgcolor("black")
turtle.tracer(0)
for x in range(10000):
    t.pencolor(colors[x%6])
    t.forward(x*1.1)
    t.left(59)
    turtle.update()
turtle.done()
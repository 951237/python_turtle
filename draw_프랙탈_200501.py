import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.back(100)
t.pendown()

def draw(l):
    if l < 10:
        return
    else:
        t.forward(l)
        t.left(30)
        draw(4*l/5)
        t.right(60)
        draw(4*l/5)
        t.left(30)
        t.back(l)

draw(100)
input()
turtle.done()

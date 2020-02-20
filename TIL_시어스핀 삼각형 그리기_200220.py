import turtle, time

wn = turtle.Screen()
t = turtle.Turtle()
t.speed()

v_dis = 100


def draw_tri(v_dis):
    for _ in range(3):
        t.forward(v_dis)
        t.left(120)

draw_tri(v_dis)
t.setpos(100,0)
draw_tri(v_dis)
t.setpos(50,100)
draw_tri(v_dis)
t.setpos(0,0)


time.sleep(5)
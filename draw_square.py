# 도형그리기 반복하여그리

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)


def d_sqare():  # 사각형 그리기
    for i in range(4):
        t.left(90)
        t.forward(150)


def d_triangle():  # 삼각형 그리기
    for i in range(3):
        t.forward(150)
        t.left(120)


def d_six():  # 6각형 그리기
    for i in range(6):
        t.forward(150)
        t.left(60)


def d_want(want, angle):  # 원하는 도형 그리기
    for i in range(want):
        t.forward(100)
        t.left(angle)


def d_want_loop(v_loop, v_angle, v_distance):  # 일정한 중심에서 원하는 도형 반복하여 그리기
    for i in range(v_loop):
        d_want(100, 3.6)
        t.penup()
        t.right(v_angle)
        t.forward(v_distance)
        t.pendown()


d_want(4, 90)

wn.mainloop()

# 도형그리기 반복하여그리

import turtle, time

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


def d_move(v_angle, v_distance): # 일정하게 각도로 주어진 거리만큼 이동하기
    t.penup()
    t.right(v_angle)
    t.forward(v_distance)
    t.pendown()


for i in range(10):
    d_want(5, 72)
    d_move(36, 50)

time.sleep(5)
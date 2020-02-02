# 선으로 원그리

import time
import turtle

ws = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.shape(name='turtle')

v_want_line = 10  # 원하는 라인의 갯수
v_want_angle = 360 / v_want_line  # 원하는 라인을 360도로 그리는데 필요한 각 계


def d_line(v_line, v_angle):
    for i in range(v_line):
        t.forward(200)
        t.left(180)
        t.forward(200)
        t.left(180 + v_angle)  # 10도 간격으로 그리고 싶으면 180 + 10 = 190


d_line(v_want_line, v_want_angle)

time.sleep(5)

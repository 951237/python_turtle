import turtle
import time

tt = turtle.Turtle()
wn = turtle.Screen()
tt.speed(0)

dis = 40

def draw_tri(dis):
	for i in range(3):
		tt.forward(dis)
		tt.left(120)

def draw_3_tri(dis):
	draw_tri(dis)
	tt.right(120)
	draw_tri(dis)
	tt.left(120)
	tt.penup()
	tt.forward(dis)
	tt.pendown()
	tt.right(120)
	draw_tri(dis)

def move_start_point(i):
	tt.penup()
	tt.right(60)
	tt.forward(dis * (2 * i - 1))
	tt.left(60)
	tt.forward(dis * 2)
	tt.pendown()
	tt.left(120)

def move_point():
	tt.penup()
	tt.left(120)
	tt.forward(dis)
	tt.pendown()

# k = 2
#
#
# for l in range(k):
# 	draw_3_tri(dis)
# 	move_start_point(l + 1)  # 1번 째 시작점 이동
# 	for i in range(k - 1):
# 		# draw_3_tri(dis)  # 삼각형 그리기
# 		move_point()  # 2번째 시작점 이동
# 		draw_3_tri(dis)

# row 1 - 삼각형 1개
draw_3_tri(dis)

# # row 2 - 삼각형 2개
move_start_point(1) # 1번 째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기
move_point()        # 2번째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기

# # row 3 - 삼각형 그리기
move_start_point(2) # 1번 째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기
move_point()        # 2번째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기
move_point()        # 3번째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기

# # row 4 - 삼각형 그리기
move_start_point(3) # 1번 째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기
move_point()        # 2번째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기
move_point()        # 3번째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기
move_point()        # 4번째 시작점 이동
draw_3_tri(dis)     # 삼각형 그리기

wn.mainloop()
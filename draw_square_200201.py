import turtle   #터틀 그래픽 모듈 호출

wm = turtle.Screen()    #터틀 스크린 오브젝트 선언
t = turtle.Turtle()     # 터틀 오브젝트
t.speed(0)              # 터틀 그리기 속도

def draw_square(v_num, v_angle, v_dis):     # 도형그리기 함수 v_num * angle = 360
	for i in range(v_num):
		t.forward(v_dis)
		t.left(v_angle)

for i in range(10):
	draw_square(5, 72, 100)
	t.left(36)

wm.mainloop()

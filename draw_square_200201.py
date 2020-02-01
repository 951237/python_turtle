import turtle

wm = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

def draw_square(v_num, v_angle, v_dis):
	for i in range(v_num):
		t.forward(v_dis)
		t.left(v_angle)

for i in range(10):
	draw_square(3, 120, 100)
	t.left(36)

wm.mainloop()

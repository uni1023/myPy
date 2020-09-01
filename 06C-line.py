# 선을 반복해서 그리는 프로그램

import turtle as t


t.shape("turtle")

angle = 89              # 거북이가 왼쪽으로회전할 각도를 지정

t.bgcolor("black")
t.color("yellow")
t.speed(0)              # 거북이 속도를 가장 빠르게 지정
for x in range(200):    # x값을 0에서 199까지 바꾸면서 200번 실행
    t.forward(x)        # x만큼 앞으로 이동 (실행을 반복하면서 선이 길어짐)
    t.left(angle)       # 거북이가 왼쪽으로 angle 만큼 회전

t.exitonclick()
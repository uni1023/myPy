# 원을 반복해서 그리는 프로그

import turtle as t

t.shape("turtle")
n = 50                  # 원을 50개 그림
t.bgcolor("black")      # 배경을 검은색으로
t.color("green")        # 펜 색을 녹색으로
t.speed(0)              # 정 거북이 속도를 가장 빠르게 지정
for x in range(n):
    t.circle(80)       # 현재 위치에서 반지름이 80인 원을 그림
    t.left(360/n)       # 거북이가 360/n 만큼 회전


t.exitonclick()
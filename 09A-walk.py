# 마음대로 걷는 거북이 1


import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(500):            # 거북이를 500번 움직임
    a = random.randint(1, 360)  # 1~360에서 아무수나 골라 a에 저장
    t.setheading(a)             # 거북이 방향을 a 각도로 돌림
    t.forward(10)               # 거북이가 10 만큼 앞으로 이동

t.exitonclick()
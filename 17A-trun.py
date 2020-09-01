# 터틀런 만들기

import turtle as t
import random

te = t.Turtle()         # 악당
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()         # 먹이 초록색
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)                           # 주인공 거북이가 10만큼 앞으로 감
    ang = te.towards(t.pos())
    te.setheading(ang)                      # 악당거북익 주인공 거북이를 바라보게 함
    te.forward(9)                           # 악당 거북이가 9만큼 앞으로 이동
    if t.distance(ts) < 12:                 # 주인공과 먹이의 거리가 12보다 작으면(가까우면)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)             # 먹이를 다른곳으로 옮김
    if t.distance(te) >= 12:                # 주인공과 악당의 거리가 12 이상이면
        t.ontimer(play, 100)                # 0.1초 후 play 함수를 실행함

t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()                          # 거북이 그래픽 창이 키보드 입력을 받게 함
play()                              # play 함수를 호출해서 게임을 시작

t.mainloop()
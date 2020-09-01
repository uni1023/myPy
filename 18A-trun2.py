# 터틀런 2 만들기

# 터틀런 1에 제목, 게임시작, 게임종료, 난이도 조절, 점수 계산 등의 기능을 추가함.

import turtle as t
import random

score = 0               # 점수를 저장하는 변수
playing = False         # 현재 게임이 플레이중인지 확인하는 변수

te = t.Turtle()         # 악당 거북이
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()                       # 먹이 초록색 동글
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right():                     # 오른쪽으로 방향을 바꿈
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():                           # 게임을 실제로 플레이하는 함수
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def play():
    global score
    global playing
    t.forward(10)                      # 주인공 거북이 10만큼 앞으로 이동
    if random.randint(1, 5) == 3:      # 1~5 사이에서 뽑은 수가 3이면 (20%확률)
        ang = te.towards(t.pos())
        te.setheading(ang)             # 악당 거북이가 주인공 거북이를 바라봄
    speed = score + 5                  # 점수에 5를 더해서 속도를 올림

    if speed > 15:                     # 속도가 15는 넘지 않게 함
        speed = 15
    te.forward(speed)
    if t.distance(te) < 12:            # 주인공과 악당의 거리가 12보다 작으면 게임을 종료

        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(ts) < 12:            # 주인공과 먹이의 거리가 12보다 작으면
        score = score + 1              # 점수를 올림
        t.write(score)                 # 점수를 화면에 표시함
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)        # 먹이를 다른곳으로 옮김
    if playing:
        t.ontimer(play, 100)           # 게임 플레이중이면 0.1초 후 play 함수를 실행

def message(m1, m2):                   # 메세지를 화면에 표시하는 함수
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()                              # 거북이 그래픽 창이 키보드 입력을 받도록 함
message("Turtle Run", "[Space]")

t.mainloop()
# 다각형을 그리는 함수


import turtle as t

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)


def polygon2(n, a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)


polygon(3)              # 삼각형을 그림
polygon(5)              # 오각형을 그림


# 그림을 그리지 않고 거북이를 100만큼 이동

t.up()
t.forward(100)
t.down()

polygon2(3, 75)
polygon2(5, 100)


t.exitonclick()
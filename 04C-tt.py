# 반복 기능으로 도형을 그리는 프로그램


import turtle as t

# 삼각형 그리기
for x in range(3):  # 3번 반복
    t.forward(100)
    t.left(120)

# 사각형 그리기
for x in range(4):  # 4번 반복
    t.forward(100)
    t.left(90)

# 원 그리기
t.circle(50)        # 반지름이 50 인 원을 그림
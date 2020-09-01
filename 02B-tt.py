# 거북이 그래픽으로 도형을 그리는 프로그램

import turtle as t


# 삼각형 그리기
t.forward(100)      # 100만큼 앞으로 이동
t.left(120)         # 120도 회전
t.forward(100)      # 위 과정을 두번 반복
t.left(120)
t.forward(100)
t.left(120)

# 사각형 그리기
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# 원 그리기

t.circle(50) # 반지름이 50인 원을 그림

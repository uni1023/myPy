# 거북이로 그림그리면서 색깔 구분하기

import turtle as t

# 삼각형 그리기
t.color("red")      # 펜 색상을 빨간색으로 변경 
t.forward(100)      # 100만큼 앞으로 이동 
t.left(120)         # 120도 회전
t.forward(100)      # 위 과정을 두번 반복 
t.left(120)
t.forward(100)
t.left(120)

# 사각형 그리기
t.color("green")    # 펜 색상을 초록색으로 변경 
t.pensize(3)        # 펜 굵기를 3으로 변경 
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# 원 그리기 
t.color("blue")     # 펜 색상을 파란색으로 변경
t.pensize(5)        # 펜 굵기를 5로 변
t.circle(50) # 반지름이 50인 원을 그림

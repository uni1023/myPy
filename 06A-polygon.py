# 정오각형을 그리는 프로그램


import turtle as t

n = 12                   # n각형을 그림
t.color("purple")
t.begin_fill()          # 색칠할 영역을 시작
for x in range(n):
    t.forward(50)
    t.left(360/n)       # 정n각형은 n개의 외각 공식
t.end_fill()            # 색칠할 영역을 마무리
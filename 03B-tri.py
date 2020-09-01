# 변수를 사용해서 삼각형을 그리는 프로그램

import turtle as t

d = 100           # 변수 d에 값 100을 저장(수치를 바꾸면 삼각형의 크기가 변함)

# 삼각형 그리기
t.forward(d)      # d만큼 앞으로 이동
t.left(120)         # 120도 회전
t.forward(d)      # 위 과정을 두번 반복
t.left(120)
t.forward(d)
t.left(120)

# 도형에서의 확률 실험 프로그램


import random

total = 1000000                 # 실험을 백만번 진행
ev = 0                          # 뽑힌 점이 사분원 안에 있는 횟수

for i in range(total):          # total 횟수만큼 반복
    x = random.random()         # 0.0 <= x < 1.0 인 실수
    y = random.random()         # 0.0 <= y < 1.0 인 실수

    if x * x + y * y <= 1.0:    # 원점과의 거리가 1 이하인 경우
        ev = ev + 1             # 사분원 안에 있는 횟수를 1 증가

print((ev / total) * 4)         # ev를 total로 나눈 평균에 4를 곱해서 출력
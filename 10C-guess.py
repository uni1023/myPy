# 숫자를 추측해서 맞히느 프로그램

import random

n = random.randint(1, 30)       # 1~30 사이에 있는 임의의 수를 뽑음

while True:                     # 영원히 반복
    x = input("맞혀 보세요? ")
    g = int(x)

    if g == n:
        print("정답")
        break
    if g < n:
        print("너무 작아요.")
    if g > n:
        print("너무 커요.")

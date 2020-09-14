
# '절댓값 구하기'

# 문제 : 어떤 숫자의 절댓값 구하기
# 입력 : 절댓값을 구할 실수 a
# 출력 : a의 절댓값

# 1 a가 0보다 크거나 같은지 확인함. 만약 그렇다면 a를 결과로 돌려줌
# 2 1의 경우가 아니라면(a가 0보다 작으면) -a를 결과로 돌려줌

import math

#절댓값 알고리즘 1(부호 판단)

# 입력: 실수 a
# 출력: a의 절댓값

def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a

# 절댓값 알고리즘 2(제곱-제곱근)
# 입력: 실수 a
# 출력: a의 절댓값


def abs_square(a):
    b = a * a
    return math.sqrt(b) # 수학 모듈의 제곱근 함수

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))




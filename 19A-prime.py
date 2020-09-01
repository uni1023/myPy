# 소인수분해를 하는 프로그램


x = int(input("?")) # 소인수 분해할 숫자를 입력받아 정수로 바꿈
d = 2               # 가장 작은 소수인 2부터 나눔

while d <= x:
    if x % d == 0:  # x가 d로 나누어지면(나머지가 0이면)
        print(d)    # d는 x의 약수이므로 출력함
        x = x / d   # x를 d로 나눠 다시 x에 저장
    else:
        d = d + 1   # 나누어지지 않으면 1을 더해서 반복
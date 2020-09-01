# 마음대로 걷는 거북이 2

import random

a = random.randint(1, 30)
b = random.randint(1, 30)

print(a, "+", b, "=")
x = input()
c = int(x)

if a + b == c:
    print("천재!")
else:
    print("바보?")


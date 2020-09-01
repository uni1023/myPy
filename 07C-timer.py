# 속으로 20초를 세어 맞히는 프로그램

import time as t

input("엔터를 누르고 20초를 셉니다.")
start = t.time()

input("20초 후에 다시 엔터를 누릅니다.")
end = t.time()

et = end - start                    # end 시간에서 start 시간을 빼면 실제 걸린 시간을 계산할 수 있습니다.
print("실제 시간 :", et, "초")
print("차이 :", abs(et - 20), "초")    # abs는 절댓값을 구하는 파이썬 기능, 계산 결과는 + - 부호를 뺀 값이 됨
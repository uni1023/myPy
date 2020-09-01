# 마우스로 거북이를 조종해서 그림 그리기


import turtle as t


t.speed(0)
t.pensize(2)
t.hideturtle()
t.onscreenclick(t.goto)     # 마우스를 누르면 t.goto 함수를 호출함
                            # 그 위치로 거북이 가 움직이면서 선을 그

t.mainloop()
from turtle import *

for i in range(3,7):
    if i%2 == 0:
        color("red")
    else:
        color("blue")
    for n in range(i):
        forward(100)
        a = 180*(i-2)/i
        left(180-a)
mainloop()

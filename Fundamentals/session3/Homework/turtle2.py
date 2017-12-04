#Cai nay dep hon de bai nen minh xin phep duoc lam cai nay
from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey', 'green', 'orange', 'purple']

for h in range(2):
    for i in range(len(colors), 0, -1):
        color(colors[i-1])
        begin_fill()
        for j in range((i+2), 0, -1):
            forward(100)
            a = 180*(i)/(i+2)
            if h%2 ==0:
                left(180-a)
            else:
                right(180-a)
        end_fill()

mainloop()

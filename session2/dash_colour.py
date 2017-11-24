from turtle import *

width(5)
n = int(input("Enter your number:"))
for i in range(n):
    if i%6 < 3:
        color('red')
    else:
        color('green')
    forward(20)
    # penup()
    # forward(20)
    # pendown()


mainloop()

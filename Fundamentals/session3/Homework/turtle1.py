from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(len(colors)):
    color(colors[i])
    for j in range(i+3):
        forward(100)
        a = 180*(i+1)/(i+3)
        left(180 - a)

mainloop()

from turtle import *

def draw_star(x, y, length):
    goto(x, y)
    for i in range(5):
        forward(length)
        left(144)

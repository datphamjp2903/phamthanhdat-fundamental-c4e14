from random import *
from bt11 import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    words = ['BLUE', 'RED', 'YELLOW', 'GREEN']
    colors = ['#3F51B5', '#C62828', '#FFD600', '#4CAF50']
    return [
                choice(words),
                choice(colors),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    user_click = [x, y]
    if quiz_type == 0:
        if text == 'BLUE':
            answer = shapes[0]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False
        elif text == 'RED':
            answer = shapes[1]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False
        elif text == 'YELLOW':
            answer = shapes[2]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False
        else:
            answer = shapes[3]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False

    else:
        if color == '#3F51B5':
            answer = shapes[0]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False
        elif color == '#C62828':
            answer = shapes[1]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False
        elif color == '#FFD600':
            answer = shapes[2]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False
        else:
            answer = shapes[3]['rect']
            check = is_inside(user_click, answer)
            if check:
                return True
            else:
                return False

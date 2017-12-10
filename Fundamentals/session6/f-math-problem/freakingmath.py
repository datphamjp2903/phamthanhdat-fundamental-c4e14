from random import *
from calc import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 20)
    y = randint(1, 20)
    error = randint(-1, 1)
    op = choice(['+', '-', '*', '/'])
    result = eval(x, y, op) + error
    return [x, y, op, result]

# def check_answer(x, y, op, result, user_choice):
#     if user_choice == True:
#         if result == eval(x, y, op):
#             return True
#         else:
#             return False
#     else:
#         if result == eval(x, y, op):
#             return False
#         else:
#             return True

# def check_answer(x, y, op, result, user_choice):
#     if user_choice: # == True
#         return result == eval(x, y, op)
#     else:
#         return not result == eval(x, y, op)

def check_answer(x, y, op, result, user_choice):
    return user_choice == (result == eval(x, y, op))

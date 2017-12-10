# import calc
#
# result = calc.eval(1, 3, '*')
# print(result)

# from calc import eval
#
# result = eval(1, 3, '-')
# print(result)

# from calc import *
#
# result = eval(2, 4, '/')
# print(result)

from calc import *
from random import *

x = randint(0, 10)
y = randint(1, 10)
op = choice(["+"]*50 + ["-"]*25 + ["*"]*10 + ["/"]*15) #xac suat
error = randint(-1, 1)
result = eval(x, y, op) + error

print('{0} {1} {2} = {3}'.format(x, op, y, result))
answer = input('Your answer: (Y/N)?').upper()
if 'Y' in answer:
    if error == 0:
        print('Yay!')
    else:
        print('Nay...')
else:
    if error == 0:
        print('Nay...')
    else:
        print('Yay!')

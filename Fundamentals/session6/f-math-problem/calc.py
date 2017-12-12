
def add(x, y): #no arguments
    print(x + y)

def eval(x, y, op): # evaluate
    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    else:
        result = x / y
    return result #cho phep dung dc bien trong def

# x = randint(0, 10)
# y = randint(1, 10)
# op = choice(['+', '-', '*', '/'])
# z = eval(x, y, op)
# print(z)

# print(__name__)


# eval(1, 2, '/')
#
# add(3, 4) #passing arguments
#
# a = 7
# b = 5
# add(a, b)
# add(2, a)

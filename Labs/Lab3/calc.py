loop = True
while loop:
    x = float(input('x = '))
    operation = input('Operation(+, -, *, /)')
    y = float(input('y = '))
    print('* ' * 20)
    if operation == "+":
        print("{0} + {1} = {2}".format(x, y, x + y))
        loop = False
    elif operation == "-":
        print("{0} - {1} = {2}".format(x, y, x - y))
        loop = False
    elif operation == "*":
        print("{0} * {1} = {2}".format(x, y, x * y))
        loop = False
    elif operation == "/":
        print("{0} / {1} = {2}".format(x, y, x / y))
        loop = False
    else:
        print("Try again")
    print('* ' * 20)

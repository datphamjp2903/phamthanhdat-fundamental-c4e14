from random import *
loop = True
point = 0
while True:
    x = randint(0, 20)
    y = randint(0, 20)
    error = randint(-1, 1)
    ope = ['+', '-', '*', '/']
    operation = choice(ope)
    if operation == "+":
        result = x + y + error
        print("{0} + {1} = {2}".format(x,y,result))
        answer = input("Y/N?")

        if error == 0:
            if answer == "Y":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break
        else:
            if answer == "N":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break
    elif operation == "-":
        result = x - y + error
        print("{0} - {1} = {2}".format(x,y,result))
        answer = input("Y/N?")

        if error == 0:
            if answer == "Y":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break
        else:
            if answer == "N":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break

    elif operation == "*":
        result = x * y + error
        print("{0} * {1} = {2}".format(x,y,result))
        answer = input("Y/N?")

        if error == 0:
            if answer == "Y":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break
        else:
            if answer == "N":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break

    else:
        result = x / y + error
        print("{0} / {1} = {2}".format(x,y,result))
        answer = input("Y/N?")

        if error == 0:
            if answer == "Y":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break
        else:
            if answer == "N":
                print("Yay!")
                point += 1
                print("Your point:", point)
            else:
                print("Nay!")
                loop = False
                break

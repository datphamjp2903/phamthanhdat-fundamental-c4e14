from random import randint
number = randint(0, 100)
guess_wrong = True #Flag
count = 0

while True and count < 7:
    guess = int(input("Enter a number (0~100):"))
    if guess > number:
        print("Too large.")
    elif guess < number:
        print("Too small.")
    else:
        print("Bingo")
        break
    count += 1
print("Lose")

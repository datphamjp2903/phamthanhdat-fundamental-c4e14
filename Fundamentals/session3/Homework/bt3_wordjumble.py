from random import choice
print("Welcome to Word Jumble")
group = [
    "Izakaya",
    "Japanese",
    "Sushi",
    "Kyoto",
    "Osaka",
    "Foreign friends"
]
words = choice(group)
jumble = []
guess =[]

for i in range(len(words)):
    word = words[i]
    jumble.append(word)

for j in range(len(jumble)):
    word_x = choice(jumble)
    jumble.remove(word_x)
    guess.append(word_x)
print("Your word: ", guess)

loop = True
while loop:
    user_guess = input("What do you think? ")
    if words == group[0]:
        if user_guess != "Izakaya":
            print("Stupid! Guess again: ")
        else:
            print("Bingo!")
            loop = False
    elif words == group[1]:
        if user_guess != "Japanese":
            print("Stupid! Guess again: ")
        else:
            print("Bingo!")
            loop = False
    elif words == group[2]:
        if user_guess != "Sushi":
            print("Stupid! Guess again: ")
        else:
            print("Bingo!")
            loop = False
    elif words == group[3]:
        if user_guess != "Kyoto":
            print("Stupid! Guess again: ")
        else:
            print("Bingo!")
            loop = False
    elif words == group[4]:
        if user_guess != "Osaka":
            print("Stupid! Guess again: ")
        else:
            print("Bingo!")
            loop = False
    else:
        if user_guess != "Foreign Friends":
            print("Stupid! Guess again: ")
        else:
            print("Bingo!")
            loop = False

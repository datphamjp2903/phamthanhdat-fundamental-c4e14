from random import choice
print("Welcome to Word Jumble")
group = [
    ["I", "z", "a", "k", "a", "y", "a"],
    ["J", "a", "p", "a", "n", "e", "s", "e"],
    ["S", "u", "s", "h", "i"],
    ["K", "y", "o", "t", "o"],
    ["O", "s", "a", "k", "a"],
    ["F", "o", "r", "e", "i", "g", "n", "f", "r", "i", "e", "n", "d", "s"]
]
words = choice(group)
guess =[]

for i in range(len(words)):
    word = choice(words)
    words.remove(word)
    guess.append(word)
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

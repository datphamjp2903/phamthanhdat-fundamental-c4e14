ft = ["Japanese", "Travel", "Sushi"]
print("Your favourite list:")
for i, fav in enumerate(ft):
    print(i+1, fav, sep=". ")

loop = True
while loop:
    delete = int(input("Delete:")) #delete number of value
    if delete < 1 or delete > len(ft):
        print("Out of range")
    else:
        ft.pop(delete - 1)
        for i, fav in enumerate(ft):
            print(i+1, fav, sep=". ")
            loop = False

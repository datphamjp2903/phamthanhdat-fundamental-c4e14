ft = ["Japanese", "Travel", "Sushi"]
print("Your favourite list:")
for i, fav in enumerate(ft):
    print(i+1, fav, sep=". ")

loop = True
while loop:
    remove = input("Favourite stuff you want to get rid of:") #remove list's item
    if remove != fav in ft: #hoac if remove not in ft:
        print("Khong co trong list")
    else:
        ft.remove(remove)
        for i, fav in enumerate(ft):#index + item cua list
            print(i+1, fav, sep=". ")
            loop = False

ft = ["Japanese", "Travel", "Sushi"]
print("Your favourite list:")
for i, fav in enumerate(ft):
    print(i+1, fav, sep=". ") #separator - noi giua cac phan tu

position = int(input("Enter position you want to update:"))
new_fav = input("Replacing fav?")

ft[position - 1] = new_fav

for i, fav in enumerate(ft):
    print(i+1, fav, sep=". ")

# for item in ft: #print list's item
#     print(item)

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

# # remove = input("Favourite stuff you want to get rid of:") #remove list's item
# # loop = True
# while loop:
    # if remove != fav in ft:
    #     print("Khong co trong list")
    # else:
    #     ft.remove(remove)
    #     for i, fav in enumerate(ft):#index + item cua list
    #         print(i+1, fav, sep=". ")
    #         loop = False

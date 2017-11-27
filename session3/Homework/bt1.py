shop = ["T-shirt", "Sweater"]
sexy = True

while sexy:
    crud = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    if crud == "R":
        print("Our items: ", end="")
        print(*shop, sep=", ")
    elif crud == "C":
        c = input("Enter new item: ")
        shop.append(c)
        print("Our items: ", end="")
        print(*shop, sep=", ")
    elif crud == "U":
        u = int(input("Update positon? "))
        if u > 0 and u <= len(shop):
            u1 = input("New item? ")
            shop[u-1] = u1
            print("Our items: ", end="")
            print(*shop, sep=", ")
        else:
            print("Out of range")
    elif crud == "D":
        d = int(input("Delete positon? "))
        if d > 0 and d <= len(shop):
            shop.pop(d-1)
            print("Our items: ", end="")
            print(*shop, sep=", ")
        else:
            print("Out of range")
    else:
        sexy = False
        print("Out of sevices")

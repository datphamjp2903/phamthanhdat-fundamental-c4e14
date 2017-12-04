print("Pattern e")
w = int(input("Width:"))
h = int(input("Height:"))
for j in range(h):
    for i in range(w):
        if (i+j)%2 == 0:
            print("* ", end="")
        else:
            print("x ", end="")
    print()

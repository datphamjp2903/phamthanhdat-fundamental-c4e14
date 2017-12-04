print("Your favouritethings:")
ft = ["Japanese", "Travel", "Python"]
for i in range(1, len(ft)+1):#print
    print(i, ft[i-1], sep=". ")

p = int(input("Position you want to update:"))#replacing
r = input("Your replacing favourite:")
ft[p-1] = r
for i in range(1, len(ft)+1):
    print(i, ft[i-1], sep=". ")

d = int(input("You want to remove:"))#remove = ft.pop
ft.remove(ft[d-1])
for i in range(1, len(ft)+1):
    print(i, ft[i-1], sep=". ")

print("Your favourite things:")
ft = ["Japanese", "Travel", "Python"]
print(*ft, sep=", ") #Separator
n = input("Add one thing:")
ft.append(n)
print(*ft, sep=", ")

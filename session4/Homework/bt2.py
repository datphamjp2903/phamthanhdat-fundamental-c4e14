numbers = [1, 5, 7, 1, 8, 5, 6, 1, 8 ,8, 8]

n = int(input("Enter your numbers: "))
count = 0

for num in numbers:
    if n == num:
        count += 1
print("{0} appears {1} times in numbers.".format(n, count))

n = int(input("Months: "))

pairs_of_rabbit = {}

for i in range(-1, n+1):
    pairs_of_rabbit[i] = 0
    if i < 1:
        pairs_of_rabbit[i] = 1
    else:
        pairs_of_rabbit[i] = pairs_of_rabbit[i-1] + pairs_of_rabbit[i-2]
del pairs_of_rabbit[-1]
for month, pair in pairs_of_rabbit.items():
    print("Month {0}: {1} pair(s) of rabbit.".format(month, pair))

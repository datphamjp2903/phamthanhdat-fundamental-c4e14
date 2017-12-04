b = int(input("How many B bacterias are there? "))
t = float(input("How much time in minute will we wait? "))
count = True
i = t // 2
if i > 0:
    num_b = int(b * (2**i))
    count = False

if not count:
    print("After {0} minutes, we would have {1} bacterias.".format(t, num_b))
else:
    print("After {0} minutes, we would have {1} bacterias.".format(t, b))

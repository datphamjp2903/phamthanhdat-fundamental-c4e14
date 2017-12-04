print("Hello, my name's Dat and there are my sheep's sizes: ")
sheeps = [5, 7, 300, 90, 24, 50, 75]
print(sheeps)
# print("Now my biggest sheep has size", max(sheeps), "let's shear it.")
# # phan tiep theo
# sheeps[sheeps.index(max(sheeps))] = 8
# print("After shearing, here is my flock:")
# print(sheeps)
#phan tiep theo

for i in range(1, 5):
    print("MONTH", i)
    print("One month has passed and now here is my flock:")
    for j, sheep in enumerate(sheeps):
        sheep += 50
        sheeps[j] = sheep
    print(sheeps)
    print("Now my biggest sheep has size", max(sheeps), "let's shear it")
    sheeps[sheeps.index(max(sheeps))] = 8
    print("After shearing, here is my flock:")
    print(sheeps)

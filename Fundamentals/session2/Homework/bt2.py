n = int(input("Your number:"))
factorial = 1
if n == 0:
    print("Factorial of 0 is 1")
elif n < 0:
    print("Invalid")
else:
    for i in range(1, n+1):
        factorial  = factorial * i
    print("Factorial of", n, "is", factorial )

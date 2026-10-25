n = int(input("Enter a positive integer: "))

# Check if N is valid
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("Factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)

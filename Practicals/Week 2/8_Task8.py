n = int(input("Enter the value of N: "))

# Initialize the first two numbers in the Fibonacci series
num1, num2 = 0, 1

# Check if N is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to", n, "term:")
    print(num1)
else:
    print("Fibonacci series up to", n, "terms:")
    print(num1, num2, end=" ")

    # Generate the Fibonacci series up to the Nth term
    for _ in range(2, n):
        next_num = num1 + num2
        print(next_num, end=" ")
        num1, num2 = num2, next_num

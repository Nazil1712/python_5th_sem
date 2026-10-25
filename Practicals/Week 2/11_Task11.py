number = int(input("Enter a positive integer: "))

# Check if the number is less than 1
if number < 1:
    print("Please enter a positive integer.")
else:
    print("Divisors of", number, ":")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

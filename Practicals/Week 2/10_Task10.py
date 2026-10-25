number = int(input("Enter a positive integer: "))

# Check if the number is less than 2
if number < 2:
    print(number, "is not a prime number.")
else:
    is_prime = True

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    # Display the result
    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

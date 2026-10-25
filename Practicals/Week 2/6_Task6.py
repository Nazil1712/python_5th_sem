def is_perfect_number(num):
    # Check if the number is positive
    if num <= 0:
        return False

    # Find the divisors and calculate their sum
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    # Check if the sum of divisors is equal to the number
    if divisors_sum == num:
        return True
    else:
        return False


# Prompt the user to enter a number
number = int(input("Enter a positive integer: "))

# Check if the number is a perfect number
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")

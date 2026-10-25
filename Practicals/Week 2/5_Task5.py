num = int(input("Enter an integer: "))
sum_of_digits = 0

# Iterate through each digit of the number
while num != 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print("Sum of the digits:", sum_of_digits)

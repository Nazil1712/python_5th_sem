input_string = input("Enter a string: ")

# Initialize counters for digits and letters
digit_count = 0
letter_count = 0

# Iterate through each character in the string
for char in input_string:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

print("Letters:", letter_count)
print("Digits:", digit_count)

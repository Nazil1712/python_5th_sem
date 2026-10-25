m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
r = 184

# Generate the two-dimensional array
array = [[i * j * r for j in range(n)] for i in range(m)]

# Display the array
print("Result:")
for row in array:
    print(row)

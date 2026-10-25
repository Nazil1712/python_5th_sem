def tuple_to_string(input_tuple):
    string_representation = ''.join(str(item) for item in input_tuple)
    return string_representation

# Example usage:
my_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a string
result_string = tuple_to_string(my_tuple)
print("Tuple converted to string:", result_string)

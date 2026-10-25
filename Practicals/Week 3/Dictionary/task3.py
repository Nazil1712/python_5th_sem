def sum_dict_items(dictionary):
    total_sum = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            total_sum += value
        elif isinstance(value, dict):
            total_sum += sum_dict_items(value)  # Recursive call for nested dictionaries
    return total_sum

# Example usage:
my_dictionary = {
    "a": 10,
    "b": 20,
    "c": {
        "d": 5,
        "e": 8
    },
    "f": 15
}

result = sum_dict_items(my_dictionary)
print("Sum of all items in the dictionary:", result)

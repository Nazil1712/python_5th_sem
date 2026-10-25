def add_key_to_dict(dictionary, key, value):
    dictionary[key] = value
    return dictionary

# Example usage:
sample_dict = {0: 10, 1: 20}
new_key = 2
new_value = 30

result_dict = add_key_to_dict(sample_dict, new_key, new_value)
print("Updated Dictionary:", result_dict)

def check_key_in_dict(dictionary, key):
    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

# Example usage:
my_dictionary = {"name": "John", "age": 30, "city": "New York"}

# Key to check
key_to_check = "age"

# Call the function to check if the key exists in the dictionary
check_key_in_dict(my_dictionary, key_to_check)

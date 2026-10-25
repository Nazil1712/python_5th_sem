def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage:
dict1 = {"name": "John", "age": 30}
dict2 = {"city": "New York", "occupation": "Engineer"}
merged_dictionary = merge_dicts(dict1, dict2)
print("Merged Dictionary:", merged_dictionary)

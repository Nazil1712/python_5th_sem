def add_item_to_tuple(existing_tuple, new_item):
    new_tuple = existing_tuple + (new_item,)
    return new_tuple

# Example usage:
existing_tuple = (1, 2, 3, 4)
new_item_to_add = 5

# Add the new item to the tuple
updated_tuple = add_item_to_tuple(existing_tuple, new_item_to_add)
print("Updated Tuple:", updated_tuple)

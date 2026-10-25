def add_members_to_set(input_set, *members):
    input_set.update(members)
    return input_set

def clear_set(input_set):
    input_set.clear()
    return input_set

# Example usage:
my_set = {1, 2, 3}

# Add members to the set
updated_set = add_members_to_set(my_set, 4, 5, 6)
print("Updated Set with added members:", updated_set)

# Clear the set
cleared_set = clear_set(updated_set)
print("Cleared Set:", cleared_set)

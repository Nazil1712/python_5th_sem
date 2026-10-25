def concatenate_dicts(*dicts):
    result_dict = {}
    for d in dicts:
        result_dict.update(d)
    return result_dict

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries
concatenated_dict = concatenate_dicts(dic1, dic2, dic3)
print("Concatenated Dictionary:", concatenated_dict)

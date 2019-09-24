


def merge_dict_sum(dict1, dict2):
    """
    Merge two dictionaries and add values of common keys.
    """
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = value + dict1[key]
    return dict3
    
def merge_dict_list(dict1, dict2):
    """
    Merge two dictionaries and add values of common keys.
    """
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value, dict1[key]]
    return dict3
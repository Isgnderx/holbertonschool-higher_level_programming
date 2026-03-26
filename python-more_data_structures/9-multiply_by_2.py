#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    """Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary to multiply.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    if a_dictionary is None:
        return None

    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2

    return new_dict

#!/usr/bin/python3

def search_replace(my_list, search, replace):

    sorted_list = my_list.copy()
    for i in range(len(sorted_list)):
        if sorted_list[i] == search:
            sorted_list[i] = replace
    return sorted_list

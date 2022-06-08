#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for run in range(len(new)):
        if new[run] == search:
            new[run] = replace
    return(new)

#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_set = set()

    # Iterate over each element in the list
    for num in my_list:
        # Add the unique integers to the set
        unique_set.add(num)

    # Calculate the sum of unique integers
    result = sum(unique_set)

    return result

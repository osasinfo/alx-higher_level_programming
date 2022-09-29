#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_integer = []
    for x in my_list:
        if x not in unique_integer:
            unique_integer.append(x)
    for x in unique_integer:
        sum += x
    return (sum)

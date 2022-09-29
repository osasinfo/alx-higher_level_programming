#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dicT in sorted(a_dictionary):
        print("{}: {}".format(dicT, a_dictionary[dicT]))

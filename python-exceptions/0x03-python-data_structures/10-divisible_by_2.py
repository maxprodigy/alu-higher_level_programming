#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multipleOfTwo = []
    for i in my_list:
        is_div = False
        if (i % 2) == 0:
            is_div = True
        multipleOfTwo.append(is_div)
    return multipleOfTwo

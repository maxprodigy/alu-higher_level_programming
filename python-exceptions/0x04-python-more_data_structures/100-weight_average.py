#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    number = [item[0] * item[1] for item in my_list]
    divisor = [item[1] for item in my_list]
    return (sum(number)/sum(divisor))

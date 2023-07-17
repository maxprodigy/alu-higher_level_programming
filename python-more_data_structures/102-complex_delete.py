#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary)
    for i in range(len(key_list)):
        if a_dictionary[key_list[i]] == value:
            del a_dictionary[key_list[i]]
    return (a_dictionary)

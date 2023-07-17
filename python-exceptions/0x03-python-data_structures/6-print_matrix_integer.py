#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for item in matrix:
        length = len(item)
        for j in range(len(item)):
            if j == length - 1:
                print("{:d}".format(item[j]),)
            else:
                print("{:d}".format(item[j]), end=" ")

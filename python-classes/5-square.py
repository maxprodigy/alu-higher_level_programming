#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Square represents an instance of a square shape'''

    def __init__(self, size=0):
        '''Initializes a new square object

           Args:
                size (int): The size of the square.
        '''
        self.size = size

    def area(self):
        '''
           Computes the area of the square based on the size.

           Returns:
               The value of the area (int).
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''
           Retrieves the value of size
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''
           Sets the value of private attribute size
        '''
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''
           Prints graphic representaion of square instance
        '''
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print("")

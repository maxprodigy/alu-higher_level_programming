#!/usr/bin/python3
'''
Defines new class
'''


class LockedClass:
    '''Class: LockedClass does not allow user to create instance of class attr
    '''
    __slots__ = ['first_name']

#!/usr/bin/python3
'''
Defines a new class called Node
'''


class Node:
    '''
    Node serves as a singly linked list
    '''

    def __init__(self, data, next_node=None):
        '''
        Initializes new data
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''
        Retrieves the value of data

        Return:
           The current value of instance data (int).
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        Checks and sets the value of data

        Args:
           value (int): The integer to be saved into data
        '''
        if (type(value) == int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        '''
        Retrieves the value of next_node

        Returns:
           The current value of next_node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        Checks and sets the value of next_node.

        Args:
          value (Node): New value to be set.
        '''
        if (type(value) == Node or value is None):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''
    A class to manage singly linked list operations
    '''
    def __init__(self):
        '''
        Initializes data into the new singly linked list
        '''
        self.__head = None

    def __str__(self):
        '''
        Prints all the memebers of the singly linked list on a separate line
        '''
        res = []
        ptr = self.__head
        while (ptr):
            res.append(str(ptr.data))
            ptr = ptr.next_node
        return ("\n".join(res))

    def sorted_insert(self, value):
        '''
        inserts a new Node into the correct sorted position in the
        list (increasing order)

        Args:
           value (int): New data to be inserted into list
        '''
        if not isinstance(value, int):
            raise TypeError("Value has to be an int")
        if self.__head is None:
            self.__head = Node(value)
        elif self.__head.data > value:
            new = Node(value, self.__head)
            self.__head = new
        else:
            ptr = self.__head
            while (ptr.next_node is not None and ptr.next_node.data < value):
                ptr = ptr.next_node
            new = Node(value, ptr.next_node)
            ptr.next_node = new

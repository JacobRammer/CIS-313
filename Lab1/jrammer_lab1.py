"""
Jacob Rammer
Class file for stacks and queues
1/28/2020
"""

from mealticket import *


class Queue:
    """
    A standard queue class. First in first out
    Check for edge cases in init
    """

    def __init__(self, size):
        """
        Init method for queue class.
        :param size: the max size of the queue
        :return: void
        """

        if not isinstance(size, int) or size <= 0:
            size = 0  # checking for string or negative number
        self.head = None
        self.tail = None
        self.maxSize = size
        self.currentSize = 0
        # self.data = []  # will need to change datatype to linked list later

    def isEmpty(self):
        """
        Checks to see if the current queue is empty
        :return: true if empty, otherwise false
        """

        return self.currentSize == 0

    def isFull(self):
        """
        Checks to see if the current queue is full
        :return: true if full, otherwise false
        """

        return self.maxSize == self.currentSize

    def front(self):
        """
        Display the front mealticket if the queue has data.
        If the queue is empty, return false. Do not modify
        the dataset.
        :return: mealticket or false
        """

        if self.isEmpty():
            return False
        return self.head.data

    def enqueue(self, ticket):
        """
        Enqueue a mealticket. Move the tail pointer back 1 and increase size
        :param ticket: Mealticket
        :return: true if successful, otherwise false
        """

        if isinstance(ticket, MealTicket):  # will only enqueue meal tickets
            if self.isFull():
                return False
            if self.tail is None:  # node is empty
                self.head = Node(ticket)
                self.tail = self.head
            else:
                self.tail.next = Node(ticket)
                self.tail = self.tail.next
            self.currentSize += 1
            return True
        return False  # if ticket is not a mealticket

    def dequeue(self):
        """
        Remove the ticket at the front of the queue
        :return: mealticket if queue has data, false if queue is empty
        """

        if self.isEmpty():
            return False
        ticket = self.head.data
        self.head = self.head.next
        self.currentSize -= 1
        return ticket


class Stack:
    """
    Stacks are first in last out
    Check for edge cases in init
    """

    def __init__(self, size):
        """
        Init method for stack class. lifo
        :param size: int, size of stack
        """

        if not isinstance(size, int) or size <= 0:
            size = 0  # checking for string or negative number
        self.head = None
        self.maxSize = size
        self.currentSize = 0
        # self.data = []  # need to change to linked list

    def isEmpty(self):
        """
        Checks to see if the stack is empty
        :return: True is empty, otherwise false
        """

        return self.currentSize == 0

    def isFull(self):
        """
        Checks to see if the stack is full
        :return: true if full, otherwise false
        """

        return self.currentSize == self.maxSize

    def push(self, ticket):
        """
        If the stack is empty, append the newest data to top of the stack
        :return: True if successful, otherwise false
        """

        if isinstance(ticket, MealTicket):  # will only push meal tickets
            if self.isFull():
                return False
            if self.head is None:
                self.head = Node(ticket)
            else:
                new_node = Node(ticket)
                new_node.next = self.head  # lifo
                self.head = new_node
            self.currentSize += 1
            return True
        return False

    def pop(self):
        """
        Get the last datatype from the top of the stack.
        :return: Mealticket if stack has data, otherwise false
        """

        if self.isEmpty():
            return False
        temp_val = self.head
        self.head = self.head.next
        temp_val.next = None
        self.currentSize -= 1
        return temp_val.data

    def peek(self):
        """
        Peek at the first element of the stack without deleting the item
        :return: Mealticket if stack has data, otherwise false
        """

        if self.isEmpty():
            return False
        return self.head.data


class Node:
    """
    This class will be the node for the linked list
    """

    def __init__(self, data):
        """
        Node class for a linked list skeleton.
        :param data: Stack or Queue object
        """

        self.data = data
        self.next = None  # Just like ll in c, start as NULL

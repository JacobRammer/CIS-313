from mealticket import *


class Queue:
    """
    A standard queue class. First in first out
    """

    def __init__(self, size: int):
        """
        Init method for queue class.
        :param size: the max size of the queue
        :return: void
        """

        self.head = 0
        self.max_size = size
        self.tail = self.max_size - 1
        self.current_size = 0
        self.data = []  # will need to change datatype to linked list later

    def is_empty(self) -> bool:
        """
        Checks to see if the current queue is empty
        :return: true if empty, otherwise false
        """

        return self.current_size == 0

    def is_full(self) -> bool:
        """
        Checks to see if the current queue is full
        :return: true if full, otherwise false
        """

        return self.max_size == self.current_size

    def front(self) -> MealTicket or False:
        """
        Display the front mealticket if the queue has data.
        If the queue is empty, return false
        :return: mealticket or false
        """

        if self.is_empty():
            return False
        return self.data[self.head]

    def enqueue(self, ticket: str) -> bool:
        """
        Enqueue a mealticket. Move the tail pointer back 1 and increase size
        :param ticket: Mealticket
        :return: true if successful, otherwise false
        """

        if self.is_full():
            return False
        self.tail = (self.tail + 1) % self.max_size
        self.data.append(ticket)
        self.current_size += 1
        return True

    def dequeue(self) -> MealTicket or False:
        """
        Remove the ticket at the front of the queue
        :return: mealticket if queue has data, false if queue is empty
        """

        if self.is_empty():
            return False
        ticket = self.data[self.head]
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return ticket


class Stack:
    """
    Stacks are first in last out
    """

    def __init__(self, size: int):
        self.head = 0
        self.max_size = size
        self.current_size = 0
        self.data = []  # need to change to linked list

    def is_empty(self) -> bool:
        """
        Checks to see if the stack is empty
        :return: True is empty, otherwise false
        """

        return self.current_size == 0

    def is_full(self) -> bool:
        """
        Checks to see if the stack is full
        :return: true if full, otherwise false
        """

        return self.current_size == self.max_size

    def push(self, ticket: str) -> bool:
        """
        If the stack is empty, append the newest data to top of the stack
        :return: True if successful, otherwise false
        """

        if self.is_full():
            return False
        self.data.append(ticket)
        self.current_size += 1
        self.head += 1

    def pop(self) -> MealTicket or False:
        """
        Get the last datatype from the top of the stack.
        :return: Mealticket if stack has data, otherwise false
        """

        if self.is_empty():
            return False
        self.head -= 1
        self.current_size -= 1
        return self.data[self.head]

    def peek(self) -> MealTicket or False:
        """
        Peek at the first element of the stack without deleting the item
        :return: Mealticket is stack has data, otherwise false
        """

        if self.is_empty():
            return False
        return self.data[0]


def main():
    test = Queue(2)
    # print(test.is_empty())
    # print(test.is_full())
    # print(test.enqueue("test"))
    # print(test.dequeue())

    stack = Stack(2)
    # stack.current_size = 2
    # print(stack.is_empty())
    # print(stack.is_full())
    print(stack.push("test"))
    # print(stack.pop())
    # print(stack.pop())
    print(stack.peek())


main()

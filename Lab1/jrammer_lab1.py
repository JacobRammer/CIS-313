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

        self.head = None
        self.tail = None
        self.max_size = size
        self.current_size = 0
        # self.data = []  # will need to change datatype to linked list later

    def isEmpty(self) -> bool:
        """
        Checks to see if the current queue is empty
        :return: true if empty, otherwise false
        """

        return self.current_size == 0

    def isFull(self) -> bool:
        """
        Checks to see if the current queue is full
        :return: true if full, otherwise false
        """

        return self.max_size == self.current_size

    def front(self) -> MealTicket or False:
        """
        Display the front mealticket if the queue has data.
        If the queue is empty, return false. Do not modify
        the dataset.
        :return: mealticket or false
        """
        # TODO fix this

        if self.isEmpty():
            return False
        return self.head.data

    def enqueue(self, ticket: MealTicket) -> bool:
        """
        Enqueue a mealticket. Move the tail pointer back 1 and increase size
        :param ticket: Mealticket
        :return: true if successful, otherwise false
        """

        if self.isFull():
            return False
        if self.tail is None:
            self.head = Node(ticket)
            self.tail = self.head
        else:
            self.tail.next = Node(ticket)
            self.tail = self.tail.next
        self.current_size += 1
        return True
        # self.data.append(ticket)
        # self.current_size += 1
        # return True

    def dequeue(self) -> MealTicket or False:
        """
        Remove the ticket at the front of the queue
        :return: mealticket if queue has data, false if queue is empty
        """

        if self.isEmpty():
            return False
        ticket = self.head.data
        self.head = self.head.next
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

    def isEmpty(self) -> bool:
        """
        Checks to see if the stack is empty
        :return: True is empty, otherwise false
        """

        return self.current_size == 0

    def isFull(self) -> bool:
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

        if self.isFull():
            return False
        self.data.append(ticket)
        self.current_size += 1
        self.head += 1

    def pop(self) -> MealTicket or False:
        """
        Get the last datatype from the top of the stack.
        :return: Mealticket if stack has data, otherwise false
        """

        if self.isEmpty():
            return False
        self.head -= 1
        self.current_size -= 1
        return self.data[self.head]

    def peek(self) -> MealTicket or False:
        """
        Peek at the first element of the stack without deleting the item
        :return: Mealticket is stack has data, otherwise false
        """

        if self.isEmpty():
            return False
        return self.data[0]


class Node:
    """
    This class will be the node for the linked list
    """

    def __init__(self, data: MealTicket):
        self.data = data
        self.next = None  # Just like ll in c, start as NULL


class LinkedList:

    def __init__(self):
        self.head = None

    def newNode(self, data: MealTicket):
        """
        Insert data at the end of the linked list
        :param data: Mealticket
        :return: void
        """

        node = Node(data)
        if self.head is None:  # if list is empty
            self.head = node.data
            return
        temp = self.head
        while temp.next:  # until None is reached
            temp = temp.next
        temp.next = node.data

    def displayList(self):
        """
        Simple method to print the linked list
        :return: void
        """

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def main():
    # test = Queue(2)
    # print(test.is_empty())
    # print(test.is_full())
    # print(test.enqueue("test"))
    # print(test.dequeue())

    # stack = Stack(2)
    # stack.current_size = 2
    # print(stack.is_empty())
    # print(stack.is_full())
    # print(stack.push("test"))
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.peek())

    # linked_list = LinkedList()
    # first = Node(1)
    # second = Node(2)
    # linked_list.newNode(first)
    # linked_list.newNode(second)
    # linked_list.displayList()

    q = Queue(4)
    print(f"Enqueue {q.enqueue(5)}")
    print(f"Enqueue {q.enqueue(4)}")
    print(f"Enqueue {q.enqueue(3)}")

    print(f"front: {q.front()}")
    print(f"Dequeue {q.dequeue()}")
    print(f"front: {q.front()}")
    print(f"Enqueue {q.enqueue(20)}")
    print(f"Dequeue {q.dequeue()}")
    print(f"Dequeue {q.dequeue()}")
    print(f"front: {q.front()}")


main()

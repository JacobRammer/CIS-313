"""
Jacob Rammer
Lab 2
2/4/2020
"""

from mealticket import *


class PriorityQueue:
    """
    Priority Queue using heaps
    """

    def __init__(self, maxS):
        """
        Constructor for PriorityQueue class
        """
        self._maxSize = maxS
        self._length = 0
        self._heap = [None]  # index starts at 1

    def __str__(self):
        """
        Author: Jared Hall    Date: 01/03/2020
        Description: Output the current queue as a string.
        Inputs: None    Outputs: str
        """

        returnValue = "Current queue: ["
        if self._length != 0:
            for ticket in self._heap:
                if ticket is None:
                    break
                else:
                    returnValue += "(" + str(ticket.ticketID) + ", "
                    returnValue += str(ticket.totalCost) + "), "
            returnValue = returnValue[:-2] + "]"
        else:
            returnValue += "]"
        return returnValue

    def isEmpty(self):
        """
        Checks to see if the PQ is empty
        :return: True if empty, else false
        """

        return self._length == 1

    def isFull(self):
        """
        Checks to see if the PQ is full
        :return: True if full, else empty
        """

        return self._length == self._maxSize

    def leftChild(self, index):
        """
        Find the index of the left child
        :param index: index of the parent
        :return: int
        """

        # index += 1  # heap index starts at 1
        return 2 * index

    def rightChild(self, index):
        """
        Returns the index of the right child
        :param index: index of the parent
        :return: int
        """

        # index += 1  # heap index start at 1
        return (2 * index) + 1

    def parent(self, index):
        """
        Get the parent of a child
        :param index: index of the child
        :return: int
        """

        return index // 2

    def insert(self, ticket):
        """
        Insert a mealticket at the end of the PQ.
        Will then need to validate the heap properties
        :param ticket: mealticket
        :return: void
        """

        if self.isFull():
            return False
        self._heap.append(ticket)
        self._length += 1
        self.heapify(self._heap, self._length, self._length)
        return True

    def heapSort(self, array):
        """
        Sort the array.
        :param array: self._heap
        :return: void
        """

        pass

    def heapify(self, heap, index, size):
        """
        Sort the heap upon insertion by using the parent index.
        :param heap: self._heap
        :param size: will just be self._length
        :param index: int
        :return: void
        """

        left_child = self.leftChild(index)
        right_child = self.rightChild(index)
        # size = self._length  # cant use size=self._length in declarations
        print(f"Left {left_child}, right {right_child}, size: {size}")
        if left_child <= size and heap[left_child] > heap[index]:
            """
            Checks for left child and checks heap properties
            """
            large = left_child
        else:
            large = index
        if right_child <= size and heap[right_child] > heap[large]:
            """
            Checks for right child"""
            large = right_child
        if large != index:
            temp = self._heap[index]
            temp2 = self._heap[large]
            self._heap[index] = temp2
            self._heap[large] = temp
            self.heapify(self._heap, large, self._length)

    def test_print(self, index):
        """
        Just a simple function for debugging to
        print stuff at the given index
        :param index: int
        :return: void
        """

        if index * 2 > self._length:
            print(f"Index of {index} is a child at the end of the tree")
            return
        if self._length % 2 == 0:
            print(f"Parent at index {index} is {self._heap[index]} "
                  f"left child is {self._heap[self.leftChild(index)]} ")
        if self._length % 2 != 0:
            print(f"Parent at index {index} is {self._heap[index]} "
                  f"left child is {self._heap[self.leftChild(index)]}, "
                  f"right child is {self._heap[self.rightChild(index)]}")


def main():
    pq = PriorityQueue(11)  # {8, 7, 6, 3, 2, 4, 5}.
    pq.insert(5)
    pq.insert(4)
    pq.insert(2)
    pq.insert(3)
    pq.insert(6)
    pq.insert(7)
    print(pq._heap)
    # pq.test_print(1)
    # pq.test_print(2)
    # pq.test_print(3)

    # print(pq.isEmpty())
    # pq._length = 1
    # print(pq.isEmpty())
    # print(pq.isFull())
    # pq._length = 5
    # print(pq.isFull())
    # del pq._heap[3]
    # for i in range(len(pq._heap)):
    #     print(pq._heap[i])


main()

"""
Jacob Rammer
Lab 02
2/8/2020
"""
from random import randint
from mealticket import *


class PriorityQueue:
    """
    Class for a priority queue using binary heaps
    """

    def __init__(self, maxSize):
        """
        Init method for pq
        :param maxSize: max size of the pq
        """

        self._maxSize = maxSize
        self._length = 0
        self._heap = []

    def isFull(self):
        """
        Check to see if the the pq if full
        :return: return true if full, else false
        """

        return self._length == self._maxSize

    def isEmpty(self):
        """
        Check to see if the pq is empty
        :return: return true if empty, else false
        """

        return self._length == 0

    def getParent(self, index):
        """
        Get the parent of the current node given the index.
        :param index: location of the node
        :return: index of the parent
        """

        return index // 2

    def getRightChild(self, index):
        """
        Get the index of the right child of node
        :param index: index of parent
        :return: index of child
        """

        return (2 * index) + 1

    def getLeftChild(self, index):
        """
        Get the index of the left child of a node
        :param index: index of parent
        :return: index of child
        """

        return 2 * index

    def heapify(self, index):
        """
        Method to make sure tree keeps binary heap properties
        when new nodes are inserted
        :param index: index of the node
        :return: void
        """

        largest = index
        leftChild = self.getLeftChild(index)
        rightChild = self.getRightChild(index)

        if self._length >= leftChild > 0:
            if self._heap[leftChild].totalCost > self._heap[largest].totalCost:
                largest = leftChild
        if self._length >= rightChild > 0:
            if self._heap[rightChild].totalCost > self._heap[largest].totalCost:
                largest = rightChild
        if largest != index:
            self._heap[index], self._heap[largest] = \
                self._heap[largest], self._heap[index]
            self.heapify(largest)

    def swap(self, index):
        """
        Swap parent and child nodes if required
        :param index: index to check
        :return: void
        """

        parent = self.getParent(index)
        while index > 0 and \
                self._heap[parent].totalCost < self._heap[index].totalCost:
            self._heap[index], self._heap[parent] = \
                self._heap[parent], self._heap[index]
            index = self.getParent(index)
            parent = self.getParent(index)

    def insert(self, ticket):
        """
        Insert new mealticket into the pq. Maintain heap properties
        Since I'm choosing to start my array at 0 (level 0) due to
        other difficulties, check to see if the heap is empty on
        push. If it is, don't need to heapify it
        :param ticket: mealticket
        :return: true if successful
        """

        if self.isFull() or type(ticket) is not MealTicket:
            return False
        self._heap.append(ticket)
        self.swap(self._length)
        self._length += 1
        return True

    def extractMax(self):
        """
        Extract the highest priority ticket. Will
        Need to heapify
        :return: Meakticket or false if empty
        """

        if self.isEmpty():
            return False
        maxTicket = self._heap[0]
        self._length -= 1
        del self._heap[0]
        self.heapify(0)
        return maxTicket

    def __str__(self):
        """
        Author: Jared Hall
        Date: 01/03/2020
        Description: Output the current queue as a string.
        Inputs: None
        Outputs: str
        """
        returnValue = "Current queue: ["
        if (self._length != 0):
            for ticket in self._heap:
                if (ticket is None):
                    break
                else:
                    returnValue += "(" + str(ticket.ticketID) + ", "
                    returnValue += str(ticket.totalCost) + "), "
            returnValue = returnValue[:-2] + "]"
        else:
            returnValue += "]"
        return returnValue

    def maximum(self):
        """
        peek at the maximum ticket
        :return: false if empty
        """

        if self.isEmpty():
            return False
        return self._heap[0]


def main():
    # pq = PriorityQueue(10)
    # pq.insert(ticket2)
    # print(pq)
    # pq.insert(ticket2)
    # print(pq)
    # for i in range(1, pq._maxSize):
    #     test = randint(1, 50)
    #     print(pq.insert(test))
    # print(pq._heap)
    # for i in range(pq._length):
    #     print(pq.extractMax())

    # print(pq._heap)
    # pq.insert(ticket1)
    # pq.insert(ticket2)
    # print(pq._heap)
    # test = pq.extractMax()
    # test2 = pq.extractMax()
    # print(test.totalCost)
    # print(test2.totalCost)
    pass


main()

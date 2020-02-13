from random import randint


class PriorityQueue:
    """
    Class for a priority queue using binary heaps
    """

    def __init__(self, maxSize):
        """
        Init methos for pq
        :param maxSize: max size of the pq
        """

        self._maxSize = maxSize + 1
        self._length = 0
        self._heap = [None] * self._maxSize

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
            if self._heap[leftChild] > self._heap[largest]:
                largest = leftChild
        if self._length >= rightChild > 0:
            if self._heap[rightChild] > self._heap[largest]:
                largest = rightChild
        if largest != index:
            self._heap[index], self._heap[largest] = \
                self._heap[largest], self._heap[index]
            self.heapify(largest)

    def increaseKey(self, index):
        """
        Swap parent and child nodes if required
        :param index: index to check
        :return: void
        """

        parent = self.getParent(index)
        while index > 1 and self._heap[parent] < self._heap[index]:
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

        if self.isFull():
            return False
        self._length += 1
        self._heap[self._length] = ticket
        self.increaseKey(self._length)
        return True

    def extractMax(self):
        """
        Extract the highest priority ticket. Will
        Need to heapify
        :return: Meakticket or false if empty
        """

        if self.isEmpty():
            return False
        maxTicket = self._heap[1]
        self._heap[1] = self._heap[self._length]
        self._length -= 1
        self.heapify(1)
        return maxTicket

    def __str__(self):
        """
        Author: Jared Hall
        Date: 01/03/2020
        Description: Output the current queue as a string.
        Inputs: None
        Outputs: str
        :return:
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


def main():
    pq = PriorityQueue(10)

    # pq.insert(5)
    # pq.insert(8)
    # pq.insert(9)
    # pq.insert((10))
    # pq.insert(6)
    # pq.insert(15)
    for i in range(1, pq._maxSize):
        test = randint(1, 50)
        print(pq.insert(test))
    print(pq._heap)
    for i in range(pq._length):
        print(pq.extractMax())


main()

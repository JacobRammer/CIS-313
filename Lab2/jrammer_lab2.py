"""
Jacob Rammer
Lab 2
2/4/2020
"""


class PriorityQueue:
    """
    Class for a priority queue using binary heaps
    """

    def __init__(self, maxSize):
        """
        init method for pq
        """

        self._maxSize = maxSize
        self._length = 0
        self._heap = [None] * (maxSize + 1)  # since idx starts @ 1

    def isFull(self):
        """
        Checks to see if the heap is full
        for successful push onto heap
        :return: true if full, else false
        """

        return self._length == self._maxSize

    def swap(self, index):
        """
        Swap the child and parent node if required to keep proper
        tree properties
        :param index: index of the node
        :param ticket: mealticket
        :return: void
        """

        # self._heap[index] = ticket
        # parent_index = self.getParent(index)
        # while index > 1 and self._heap[parent_index] < self._heap[index]:
        #     self._heap[index], self._heap[parent_index] = \
        #         self._heap[parent_index], self._heap[index]
        #     print(f"index is {index}")
        #     parent_index = self.getParent(index)
        #     index = self.getParent(index)
        # print(f"index 1 is {index}")

        parent = self.getParent(index)
        left_child = self.getLeftChild(parent)
        right_child = self.getRightChild(parent)

        if parent == 0:
            return

        if left_child <= parent and self._heap[left_child] \
                < self._heap[index]:
            largest = left_child
        else:
            largest = index
        if right_child <= parent and self._heap[right_child] \
                < self._heap[largest]:
            largest = right_child

        if largest != index:
            self._heap[index], self._heap[largest] = \
                self._heap[largest], self._heap[index]
            self.swap(largest)

    def insert(self, ticket):
        """
        Insert a mealticket into the heap while keeping
        parent child structure
        :param key: mealticket
        :return: void
        """

        if self.isFull():
            return False
        self._length += 1
        self._heap[self._length] = ticket
        self.swap(self._length)

    def getParent(self, index):
        """
        Return the index of the parent node
        :param index: int
        :return: int
        """

        return index // 2

    def getLeftChild(self, index):
        """
        Get the index of the left child
        :param index: index of parent
        :return: int
        """

        return 2 * index

    def getRightChild(self, index):
        """
        Get the index of the right child
        :param index: index of parent
        :return: int
        """

        return (2 * index) + 1


def main():
    pq = PriorityQueue(7)
    pq.insert(5)
    pq.insert(9)
    # pq.insert(4)
    # pq.insert(6)
    # pq.insert(8)

    # print(pq._length)
    # pq.insert(8)
    print(pq._heap)


main()

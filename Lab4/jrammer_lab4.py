"""
Jacob Rammer
3/7/2020
Thanks for the skeleton code!
I am opting not to use to to stay as close
to the book implementation as possible
"""

from mealticket import *


class RBNode:
    """
    Node for a red black tree
    """

    def __init__(self, ticket, color="red"):
        """
        Init method for RBNode
        :param ticket: mealticket
        :param color: color of the node
        """

        # color.lower() # cause me lazy
        ticketID = 0
        if type(ticket) is MealTicket:  # to prevent crash on declaration
            ticketID = ticket.ticketID
        self.key = ticket  # mealticket
        self.value = ticketID
        self.color = color.lower()
        self.parent = None
        self.leftChild = None
        self.rightChild = None


class RedBlackTree:
    """
    Class for Reb Black Tree data structure
    """

    def __init__(self):
        """
        Init method for RBtree. Root always starts off as black
        """

        self.nil = RBNode(None, "black")
        self._root = self.nil
        self.walk = ""

    def _leftRotate(self, CurrentNode):
        """
        Rotate a node to the left
        :param node: RBNode
        :return: void
        """

        y = CurrentNode.rightChild
        CurrentNode.rightChild = y.leftChild

        if y.leftChild != self.nil:
            y.leftChild.parent = CurrentNode
        y.parent = CurrentNode.parent
        if CurrentNode.parent == self.nil:
            self._root = y
        elif CurrentNode == CurrentNode.parent.leftChild:
            CurrentNode.parent.leftChild = y
        else:
            CurrentNode.parent.rightChild = y
        y.leftChild = CurrentNode
        CurrentNode.parent = y

    def _rightRotate(self, currentNode):
        """
        Rotate a note to the left.
        Same as _rotateLeft except left is replaced with right
        :param currentNode: RBNode
        :return: void
        """

        y = currentNode.leftChild
        currentNode.leftChild = y.rightChild

        if y.rightChild != self.nil:
            y.rightChild.parent = currentNode
        y.parent = currentNode.parent
        if currentNode.parent == self.nil:
            self._root = y
        elif currentNode == currentNode.parent.rightChild:
            currentNode.parent.rightChild = y
        else:
            currentNode.parent.leftChild = y
        y.rightChild = currentNode
        currentNode.parent = y

    def insert(self, ticket):
        """
        Insert a mealticket into the tree
        :param ticket: mealticket
        :return: True if successful, else false
        """

        returnValue = False
        if type(ticket) is MealTicket:
            ticket = RBNode(ticket)
            y = self.nil
            x = self._root
            while x != self.nil:
                y = x
                if ticket.key.ticketID < x.key.ticketID:
                    x = x.leftChild
                    returnValue = True
                else:
                    x = x.rightChild
                    returnValue = True
            ticket.parent = y
            if y == self.nil:
                self._root = ticket
                returnValue = True
            elif ticket.key.ticketID < y.key.ticketID:
                y.leftChild = ticket
                returnValue = True
            else:
                y.rightChild = ticket
                returnValue = True
            ticket.leftChild = self.nil
            ticket.rightChild = self.nil
            ticket.color = "red"
            # print(f"Z is {z}")
            # print(f"hgv {ticket}")
            self.insertFixup(ticket)
            returnValue = True

        return returnValue

    def insertFixup(self, currentNode):
        """
        Fix the tree after inserting a mealticket
        Cases:
        1: When the uncle of y is red
        2: Uncle y of the current node is black and is a right child
        3: Uncle y of the current node is black and is a left child
        :param currentNode: RBNode to perform the fixup
        :return: void
        """

        black = "BLACK"  # so that i don't have to use the shift key
        red = "RED"  # don't use anyways i guess
        # print(f"Z2 is {z}")

        while currentNode.parent.color == "red":
            # print(f"Z2 is {z}")
            if currentNode.parent == currentNode.parent.parent.leftChild:
                y = currentNode.parent.parent.rightChild
                if y.color == "red":
                    '''Case 1'''
                    currentNode.parent.color = "black"
                    y.color = "black"
                    currentNode.parent.parent.color = "red"
                    currentNode = currentNode.parent.parent
                else:
                    if currentNode == currentNode.parent.rightChild:
                        '''Case 2'''
                        currentNode = currentNode.parent
                        self._leftRotate(currentNode)
                    '''Case 3'''
                    currentNode.parent.color = "black"
                    currentNode.parent.parent.color = "red"
                    self._rightRotate(currentNode.parent.parent)
            else:  # this is the same as above but left and right swap
                y = currentNode.parent.parent.leftChild
                if y.color == "red":
                    '''Case 1'''
                    currentNode.parent.color = "black"
                    y.color = "black"
                    currentNode.parent.parent.color = "red"
                    currentNode = currentNode.parent.parent
                else:
                    if currentNode == currentNode.parent.leftChild:
                        '''Case 2'''
                        currentNode = currentNode.parent
                        self._rightRotate(currentNode)
                    '''Case 3'''
                    currentNode.parent.color = "black"
                    currentNode.parent.parent.color = "red"
                    self._leftRotate(currentNode.parent.parent)
        self._root.color = "black"

    def transplant(self, nodeOne, nodeTwo):
        """
        Transplant a node during a deletion to maintain
        RBTree properties
        :param nodeOne: RBTNode 1
        :param nodeTwo: RBTNode 2
        :return: True
        """

        if nodeOne.parent == self.nil:
            self._root = nodeTwo
        elif nodeOne == nodeOne.parent.leftChild:
            nodeOne.parent.leftChild = nodeTwo
        else:
            nodeOne.parent.rightChild = nodeTwo
        nodeTwo.parent = nodeOne.parent

        return True  # since we're just swapping, always true

    def delete(self, ticketID):
        """
        This deletes a child from a tree. Will need to
        call self.search to return the mealticket object
        since z is an int
        :param ticketID: int of MTID
        :return: true if successful, else false
        """

        returnValue = False
        tempVal = ticketID  # to validate input against 0
        ticketID = self._search(ticketID, self._root)
        if type(ticketID) is RBNode:
            # print("sdfg")
            y = ticketID
            original_color = y.color
            if ticketID.leftChild == self.nil:
                x = ticketID.rightChild
                self.transplant(ticketID, ticketID.rightChild)
            elif ticketID.rightChild == self.nil:
                x = ticketID.leftChild
                self.transplant(ticketID, ticketID.leftChild)
            else:
                y = self.min(ticketID.rightChild)
                original_color = y.color
                x = y.rightChild
                if y.parent == ticketID:
                    x.parent = y
                else:
                    self.transplant(y, y.rightChild)
                    y.rightChild = ticketID.rightChild
                    y.rightChild.parent = y
                self.transplant(ticketID, y)
                y.leftChild = ticketID.leftChild
                y.leftChild.parent = y
                y.color = ticketID.color
            if original_color == "black":
                self.deleteFixup(x)
            returnValue = True
        return returnValue

    def deleteFixup(self, CurrentNode):
        """
        Restore the properties of the RB tree upon
        node deletion
        Cases:
        1: the sibling of x, w is red
        2: The sibling of x, w is black, and the children of w is are black
        3: The sibling of x, w is black, the left child of w is red, r = red
        4: The sibling of x, w is black and the right child of w is red
        :param CurrentNode: node to check
        :return: void
        """

        while CurrentNode != self._root and CurrentNode.color == "black":
            if CurrentNode == CurrentNode.parent.leftChild:
                w = CurrentNode.parent.rightChild
                if w.color == "red":
                    '''Case 1'''
                    w.color = "black"
                    CurrentNode.parent.color = "red"
                    self._leftRotate(CurrentNode.parent)
                    w = CurrentNode.parent.rightChild
                if w.leftChild.color == "black" and w.rightChild.color == \
                        "black":
                    '''Case 2'''
                    w.color = "red"
                    CurrentNode = CurrentNode.parent
                else:
                    if w.rightChild.color == "black":
                        '''Case 3'''
                        w.leftChild.color = "black"
                        w.color = "red"
                        self._rightRotate(w)
                        w = CurrentNode.parent.rightChild
                    '''Case 4'''
                    w.color = CurrentNode.parent.color
                    CurrentNode.parent.color = "black"
                    w.rightChild.color = "black"
                    self._leftRotate(CurrentNode.parent)
                    CurrentNode = self._root
            else:  # same as above but left and right are swapped
                w = CurrentNode.parent.leftChild
                if w.color == "red":
                    '''Case 1'''
                    w.color = "black"
                    CurrentNode.parent.color = "red"
                    self._rightRotate(CurrentNode.parent)
                if w.rightChild.color == "black" and w.leftChild.color \
                        == "black":
                    '''Case 2'''
                    w.color = "red"
                    CurrentNode = CurrentNode.parent
                else:
                    if w.leftChild.color == "black":
                        '''Case 3'''
                        w.rightChild.color = "black"
                        w.color = "red"
                        self._leftRotate(w)
                        w = CurrentNode.parent.leftChild
                    '''Case 4'''
                    w.color = CurrentNode.parent.color
                    CurrentNode.parent.color = "black"
                    w.leftChild.color = "black"
                    self._rightRotate(CurrentNode.parent)
                    CurrentNode = self._root
        CurrentNode.color = "black"

    def min(self, currentTree):
        """
        Return the minimum value of the tree by traversing the left
        :param currentTree: node to traverser
        :return: Node with minimum value
        """

        while currentTree.leftChild != self.nil:
            currentTree = currentTree.leftChild
        return currentTree

    def max(self, currentTree):
        """
        Return the max mealticket based on ticketID.
        Right tree traversal
        :param currentTree: tree to traverse
        :return: node with mealticket
        """

        while currentTree.rightChild != self.nil:
            currentTree = currentTree.rightChild
        return currentTree

    def _search(self, id, node):
        """
        Return a mealticket based on the mealticket ID
        :param id: mealticket id
        :param node: current node
        :return: RBTnode for delete
        """

        returnValue = False
        # print(f"id {type(id)}")
        if type(id) is int:
            # print("he")
            while node != self.nil and node.key.ticketID != id:
                if id < node.key.ticketID:
                    node = node.leftChild
                else:
                    node = node.rightChild
            if node.key:  # so i can return false if not found
                returnValue = node
        return returnValue

    def find(self, id):
        """
        Just like search, but returns a mealticket
        :param id: id of mealticket
        :return: mealticket
        """

        returnValue = False
        node = self._root
        # print(f"id {type(id)}")
        if type(id) is int and id > 0:
            # print("he")
            while node != self.nil and node.value != id:
                if id < node.value:
                    node = node.leftChild
                else:
                    node = node.rightChild
            if node.value == id:  # so i can return false if not found
                returnValue = node.key
        return returnValue

    def traverse(self, mode):
        """
        Tree traversal depending on the mode
        :param mode: string of traversal mode
        :return: str of walk
        """

        self.walk = ""
        returnStr = ""
        if mode == "in-order":
            returnStr = self.inOrder(self._root)
        if mode == "post-order":
            returnStr = self.postOrder(self._root)
        if mode == "pre-order":
            returnStr = self.preOrder(self._root)

        return returnStr

    def preOrder(self, node):
        """
        Preorder traversal of the bst
        :param node:
        :return: string of traversal
        """

        if type(node) is RedBlackTree:
            node = self._root
        if node is not self.nil:
            self.walk += f"{str(node.key.ticketID)}: {node.color}, "
            self.preOrder(node.leftChild)
            self.preOrder(node.rightChild)
        return self.walk[:-2]

    def postOrder(self, node):
        """
        Post order traversal of the bst
        :param node: bst
        :return: string of traversal
        """

        if type(node) is RedBlackTree:
            node = self._root
        if node is not self.nil:
            self.postOrder(node.leftChild)
            self.postOrder(node.rightChild)
            self.walk += f"{str(node.key.ticketID)}: {node.color}, "
        return self.walk[:-2]

    def inOrder(self, node):
        """
        Inorder traversal on the BST
        :return: string of the traversal
        """

        if node is not self.nil:
            self.inOrder(node.leftChild)
            self.walk += f"{str(node.key.ticketID)}: {node.color}, "
            self.inOrder(node.rightChild)

        return self.walk[:-2]


def main():
    rb = RedBlackTree()
    l = generateMealTickets(10)
    j = 0
    for i in range(10):
        print(f"insert {l[i].ticketID}")
        rb.insert(l[i])
    for i in range(10):
        j = randint(1, 20)
        print(f"Delete {j}")
        rb.delete(j)
    print(rb.traverse("in-order"))
    print(rb.traverse("post-order"))
    print(rb.traverse("pre-order"))
    # ticket1.ticketID = 10
    # print(f"Insert {rb.insert(ticket1)}")
    # rb.delete(10)
    # # print(f"Insert {rb.insert(ticket3)}")
    # # print(f"Insert {rb.insert(ticket2)}")
    # # print(f"Insert {rb.insert(ticket4)}")
    # # print(f"Insert {rb.insert(ticket5)}")
    # # rb.insertFixup(rb._root)
    # # print(rb.insert(ticket6))
    # # print(rb._root.parent.rightChild)
    # # print(rb.delete(10))
    # # print(rb.find(2))
    # # print(f"Find {rb.find(18)}")
    #
    # # print(f"rb._root.color: {rb._root.color}")
    # # print(f"rb._root.key.ticketID: {rb._root.key.ticketID}")
    # #
    # # print(f"\nrb._root.rightChild.color: {rb._root.rightChild.color}")
    # # print(f"rb._root.rightChild.value: {rb._root.rightChild.value}")
    # #
    # # print(f"\nrb._root.leftChild.color: {rb._root.leftChild.color}")
    # # print(f"rb._root.leftChild.value: {rb._root.leftChild.value}")
    # #
    # print(rb.traverse("in-order"))
    # print(rb.traverse("pre-order"))
    # print(rb.traverse("post-order"))

    # print(rb._search(3, rb._root).value)
    # print(rb.)
    # # print(rb.delete(1))
    # print(rb.find(1).ticketID)
    # print("\n Delete")
    # print(f"rb._root.color: {rb._root.color}")
    # print(f"rb._root.key.ticketID: {rb._root.key.ticketID}")
    # print(f"\nrb._root.rightChild.color: {rb._root.leftChild.color}")
    # print(f"rb._root.rightChild.value: {rb._root.leftChild.value}")
    # print("\nNew insert")
    # print(f"rb._root.color: {rb._root.color}")
    # print(f"rb._root.key.ticketID: {rb._root.key.ticketID}")
    # print(f"\nrb._root.rightChild.color: {rb._root.rightChild.color}")
    # print(f"rb._root.rightChild.value: {rb._root.rightChild.value}")

    # print(rb._search(1, rb._root).value)

    # print("\nNew insert")
    # print(f"rb._root.color: {rb._root.color}")
    # print(f"rb._root.key.ticketID: {rb._root.key.ticketID}")
    #
    # print(f"\nrb._root.rightChild.color: {rb._root.rightChild.color}")
    # print(f"rb._root.rightChild.value: {rb._root.rightChild.value}")
    #
    # print(f"\nrb._root.leftChild.color: {rb._root.leftChild.color}")
    # print(f"rb._root.leftChild.value: {rb._root.leftChild.value}")

    # print(rb.min(rb._root).value)
    # print(rb.max(rb._root).value)

    # print(rb._root.rightChild.key.ticketID)
    # print(rb._root.leftChild.key.ticketID)
    # print(rb._root.parent.rightChild.color)
    # print(rb.insert(ticket1))
    # print(rb._root.key.ticketID)
    # print(rb._root.rightChild.key.ticketID)
    # print(rb._root.leftChild.key.ticketID)


if __name__ == "__main__":
    main()

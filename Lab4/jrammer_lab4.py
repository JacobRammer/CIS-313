"""
Jacob Rammer
3/8/2020
Thanks for the skeleton code!
I am opting not to use to to stay as close
to the book implementation as possible
"""

from mealticket import *


# todo remove function prototypes

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
        self.key = ticket
        self.value = ticketID
        self.color = color.lower()
        self.parent = None
        self.left = None
        self.right = None


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

    def _leftRotate(self, x):
        """
        Rotate a node to the left
        :param node: RBNode
        :return: void
        """

        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rightRotate(self, x):
        """
        Rotate a note to the left.
        Same as _rotateLeft except left is replaced with right
        :param x: RBNode
        :return: void
        """

        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self._root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

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
                    x = x.left
                    returnValue = True
                else:
                    x = x.right
                    returnValue = True
            ticket.parent = y
            if y == self.nil:
                self._root = ticket
                returnValue = True
            elif ticket.key.ticketID < y.key.ticketID:
                y.left = ticket
                returnValue = True
            else:
                y.right = ticket
                returnValue = True
            ticket.left = self.nil
            ticket.right = self.nil
            ticket.color = "red"
            # print(f"Z is {z}")
            # print(f"hgv {ticket}")
            # self.insertFixup(ticket)
            returnValue = True

        return returnValue

    def insertFixup(self, currentNode):
        """
        Fix the tree after inserting a mealticket
        :param currentNode: RBNode to perform the fixup
        :return: void
        """

        black = "BLACK"  # so that i don't have to use the shift key
        red = "RED"  # don't use anyways i guess
        # print(f"Z2 is {z}")

        while currentNode.parent.color == "red":
            # print(f"Z2 is {z}")
            if currentNode.parent == currentNode.parent.parent.left:
                y = currentNode.parent.parent.right
                if y.color == "red":
                    currentNode.parent.color = "black"
                    y.color = "black"
                    currentNode.parent.parent.color = "red"
                    currentNode = currentNode.parent.parent
                else:
                    if currentNode == currentNode.parent.right:
                        currentNode = currentNode.parent
                        self._leftRotate(currentNode)
                    currentNode.parent.color = "black"
                    currentNode.parent.parent.color = "red"
                    self._rightRotate(currentNode.parent.parent)
            else:  # this is the same as above but left and right swap
                y = currentNode.parent.parent.left
                if y.color == "red":
                    currentNode.parent.color = "black"
                    y.color = "black"
                    currentNode.parent.parent.color = "red"
                    currentNode = currentNode.parent.parent
                else:
                    if currentNode == currentNode.parent.left:
                        currentNode = currentNode.parent
                        self._rightRotate(currentNode)
                    currentNode.parent.color = "black"
                    currentNode.parent.parent.color = "red"
                    self._leftRotate(currentNode.parent.parent)
        self._root.color = "black"

    def transplant(self, u, v):
        """
        Transplant a node during a deletion to maintain
        RBTree properties
        :param u: RBTNode 1
        :param v: RBTNode 2
        :return: True
        """

        if u.parent == self.nil:
            self._root = v
        elif u == u.parent.left:
            u.parent.right = v
        else:
            u.parent.right = v
        v.parent = u.parent

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
        if ticketID > 0:
            y = ticketID
            original_color = y.color
            if ticketID.left == self.nil:
                x = ticketID.right
                self.transplant(ticketID, ticketID.right)
            elif ticketID.right == self.nil:
                x = ticketID.left
                self.transplant(ticketID, ticketID.left)
            else:
                y = self.min(ticketID.right)
                original_color = y.color
                x = y.right
                if y.parent == ticketID:
                    x.parent = y
                else:
                    self.transplant(y, y.right)
                    y.right = ticketID.right
                    y.right.parent = y
                self.transplant(ticketID, y)
                y.left = ticketID.left
                y.left.parent = y
                y.color = ticketID.color
            if original_color == "black":
                self.deleteFixup(x)
            returnValue = True
        return returnValue

    def deleteFixup(self, x):
        """
        Restore the properties of the RB tree upon
        node deletion
        :param x: node to check
        :return: void
        """

        while x != self._root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self._leftRotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                elif w.right.color == "black":
                    w.left.color = "black"
                    w.color = "red"
                    self._rightRotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = "black"
                w.right.color = "black"
                self._leftRotate(x.parent)
                x = self._root
            else:  # same as above but left and right are swapped
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self._rightRotate(x.parent)
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self._leftRotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self._rightRotate(x.parent)
                    x = self._root
        x.color = "black"

    def min(self, currentTree):
        """
        Return the minimum value of the tree by traversing the left
        :param currentTree: node to traverser
        :return: Node with minimum value
        """

        while currentTree.left != self.nil:
            currentTree = currentTree.left
        return currentTree

    def max(self, currentTree):
        """
        Return the max mealticket based on ticketID.
        Right tree traversal
        :param currentTree: tree to traverse
        :return: node with mealticket
        """

        while currentTree.right != self.nil:
            currentTree = currentTree.right
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
            while node != self.nil and node.value != id:
                if id < node.value:
                    node = node.left
                else:
                    node = node.right
            if node.value == id:  # so i can return false if not found
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
                    node = node.left
                else:
                    node = node.right
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
            self.preOrder(node.left)
            self.preOrder(node.right)
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
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.walk += f"{str(node.key.ticketID)}: {node.color}, "
        return self.walk[:-2]

    def inOrder(self, node):
        """
        Inorder traversal on the BST
        :return: string of the traversal
        """

        if node is not self.nil:
            self.inOrder(node.left)
            self.walk += f"{str(node.key.ticketID)}: {node.color}, "
            self.inOrder(node.right)

        return self.walk[:-2]


def main():
    rb = RedBlackTree()
    l = generateMealTickets(15)
    for i in range(15):
        # print(l[i])
        print(rb.insert(l[i]))
    print(rb.delete(5))
    # print(rb._search(5, rb._root))
    print(rb.traverse("in-order"))
    # print(rb.traverse("post-order"))
    # print(rb.traverse("pre-order"))
    # ticket1.ticketID = 10
    # print(f"Insert {rb.insert(ticket1)}")
    # rb.delete(10)
    # # print(f"Insert {rb.insert(ticket3)}")
    # # print(f"Insert {rb.insert(ticket2)}")
    # # print(f"Insert {rb.insert(ticket4)}")
    # # print(f"Insert {rb.insert(ticket5)}")
    # # rb.insertFixup(rb._root)
    # # print(rb.insert(ticket6))
    # # print(rb._root.parent.right)
    # # print(rb.delete(10))
    # # print(rb.find(2))
    # # print(f"Find {rb.find(18)}")
    #
    # # print(f"rb._root.color: {rb._root.color}")
    # # print(f"rb._root.key.ticketID: {rb._root.key.ticketID}")
    # #
    # # print(f"\nrb._root.right.color: {rb._root.right.color}")
    # # print(f"rb._root.right.value: {rb._root.right.value}")
    # #
    # # print(f"\nrb._root.left.color: {rb._root.left.color}")
    # # print(f"rb._root.left.value: {rb._root.left.value}")
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
    # print(f"\nrb._root.right.color: {rb._root.left.color}")
    # print(f"rb._root.right.value: {rb._root.left.value}")
    # print("\nNew insert")
    # print(f"rb._root.color: {rb._root.color}")
    # print(f"rb._root.key.ticketID: {rb._root.key.ticketID}")
    # print(f"\nrb._root.right.color: {rb._root.right.color}")
    # print(f"rb._root.right.value: {rb._root.right.value}")

    # print(rb._search(1, rb._root).value)

    # print("\nNew insert")
    # print(f"rb._root.color: {rb._root.color}")
    # print(f"rb._root.key.ticketID: {rb._root.key.ticketID}")
    #
    # print(f"\nrb._root.right.color: {rb._root.right.color}")
    # print(f"rb._root.right.value: {rb._root.right.value}")
    #
    # print(f"\nrb._root.left.color: {rb._root.left.color}")
    # print(f"rb._root.left.value: {rb._root.left.value}")
    #
    # print(f"\nrb._root.right.right.color: {rb._root.right.right.color}")
    # print(f"rb._root.right.right.value: {rb._root.right.right.value}")

    # print(rb.min(rb._root).value)
    # print(rb.max(rb._root).value)

    # print(rb._root.right.key.ticketID)
    # print(rb._root.left.key.ticketID)
    # print(rb._root.parent.right.color)
    # print(rb.insert(ticket1))
    # print(rb._root.key.ticketID)
    # print(rb._root.right.key.ticketID)
    # print(rb._root.left.key.ticketID)


main()

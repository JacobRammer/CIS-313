"""
Jacob Rammer
Lab 3
2/24/2020
LIES: you said third one is easier than
lab 2. It was not lmao
"""
from mealticket import *


class BSTNode:
    """
    This class will be the node for the linked list
    Credit: myself from lab 1 and the book
    """

    def __init__(self, ticket):
        """
        Node class for a linked list skeleton.
        :param ticket: Value to initialize Node
        """

        self.key = ticket
        self.right = None  # larger value
        self.left = None  # smaller value
        self.parent = None  # greater value

    def numChilds(self):
        """
        Debugger function that will be used in the repr.
        Calculates the how complete the tree is
        :return: number of children
        """

        number = 0
        if self.right is not None:
            number += 1
        if self.left is not None:
            number += 1
        if self.parent is not None:
            number += 1

        return number

    # def __repr__(self):
    #     """
    #     Debugging stuff
    #     :return: string
    #     """
    #
    #     string = ""
    #     if self.numChilds() == 0:  # Node is empty
    #         string = "Node is empty"
    #     elif self.numChilds() == 1:
    #         string = f"Key: {self.key} No child or parent"
    #     elif self.numChilds() == 2 and self.left is not None:
    #         string = f"Key: {self.key} Parent: {self.parent} left child: {self.left}"
    #     elif self.numChilds() == 2 and self.right is not None:
    #         string = f"Key: {self.key} Parent: {self.parent} right child: {self.right}"
    #     elif self.numChilds() == 2:
    #         string = f"Key: {self.key} Parent: {self.parent} right child: {self.right}"
    #     elif self.numChilds() == 3:
    #         string = f"Key: {self.key} Parent: {self.parent} left child: {self.left} " \
    #                  f"right child: {self.right}"
    #     return string


class BinarySearchTree:
    """
    Binary Search Tree
    Inorder traversal
    """

    def __init__(self):
        """
        Create the BST and create
        :return: void
        """

        self._root = None
        self._walk = ""

    def insert(self, ticket):
        """
        Insert a ticket into the BST while maintaining order.
        Inspired by the code in the book
        :param ticket: mealticket node
        :return: True if successful, else false
        """

        # flag = False
        # y = None
        # x = self._root
        #
        # ticket = BSTNode(ticket)
        # while x is not None:
        #     y = x
        #     if ticket.key < x.key:
        #         x = x.left
        #     else:
        #         x = x.right
        #
        # ticket.parent = y
        # if y is None:
        #     self._root = ticket
        # elif ticket.key < y.key:
        #     y.left = ticket
        # else:
        #     y.right = ticket

        ticketNode = BSTNode(ticket)
        returnVal = False  # since we're using 1 return
        if type(ticket) is not MealTicket:
            print("From insert: ticket type is not mealticket")
        else:
            if self._root is None:  # nothing in the tree
                self._root = ticketNode
                returnVal = True
            else:  # tree has elements, need to maintain order r > l
                self.recursiveInsert(ticket, self._root)
                returnVal = True
        return returnVal

    def recursiveInsert(self, ticket, root):
        """
        This method is called most of the time when inserting a node.
        Since it's easier to breakup the recursive insert method (imo),
        this is the recursive case
        :param ticket: mealticket
        :param root: parent node of the tree
        :return: true if successful, else false
        """

        flag = False
        # print(type(ticket))

        if ticket.ticketID < root.key.ticketID:  # if new value is less than
            if root.left is None:
                '''No left child'''
                root.left = BSTNode(ticket)
                root.left.parent = root
            else:
                '''Left child has a value'''
                self.recursiveInsert(ticket, root.left)
        elif ticket.ticketID > root.key.ticketID:
            if root.right is None:
                '''No right child'''
                root.right = BSTNode(ticket)
                root.right.parent = root
            else:
                self.recursiveInsert(ticket, root.right)

    def transplant(self, nodeU, nodeV):
        """
        Replaces a subtree as a child of its parent with
        another subtree.
        Credit: book
        :param nodeU: subtree 1
        :param nodeV: subtree 2
        :return: void
        """

        if nodeU.parent is None:
            '''U is the root'''
            self._root = nodeV
        elif nodeU == nodeU.parent.left:
            '''update if u has left child'''
            nodeU.parent.left = nodeV
        else:
            nodeU.parent.right = nodeV
        if nodeV is not None:
            nodeV.parent = nodeU.parent

    def deleteFind(self, id):
        """
        Function to call _find recursively because you
        can't call methods with self._root as an argument.
        Used to return the correct type for deletion which
        is a BSTNode
        :param id: id of mealticket
        :return: the BSTNode containing the MT, or false if not found
        """

        returnVal = False
        if self._root is None:
            return False
        else:
            return self._find(self._root, id) or returnVal

    def find(self, id):
        """
        Function to call _find recursively because you
        can't call methods with self._root as an argument
        :param id: id of mealticket
        :return: the mealticket, or false if not found
        """

        returnVal = False
        if type(id) is int:
            if self._root is None:
                returnVal = False
            else:
                returnVal = self._find(self._root, id)
                if returnVal is not None:
                    returnVal = returnVal.key
                else:
                    returnVal = False
        return returnVal

    def _find(self, node, id):
        """
        Search the BST and return the mealticket object if found
        Recursive function cause i cant get node=self._root to work
        :param id: int of mealticket id
        :return: mealticket if in BST, else false
        """

        returnVal = None
        # if returnVal is not False:  #
        temp = node.key.ticketID
        if id == node.key.ticketID:
            returnVal = node
        elif id < node.key.ticketID and node.left is not None:
            returnVal = self._find(node.left, id)
        elif id > node.key.ticketID and node.right is not None:
            returnVal = self._find(node.right, id)
        return returnVal

    def delete(self, ticketID):
        """
        Find the node in the tree then pass the node
        to the deleteNode method. I originally used self._root
        in the call which is why I needed this function.
        This returns the mealticket object, not BST node like
        deleteNode does.
        :param ticketID: ID of mealticket
        :return:true if successful, else false
        """

        returnVal = False
        if type(ticketID) is int:
            returnVal = self.deleteNode(self.deleteFind(ticketID))
        return returnVal

    def children(self, node):
        """
        Find the number of children in a tree
        :param bst:
        :return:
        """

        numChildren = 0
        if node.left is not None:
            numChildren += 1
        if node.right is not None:
            numChildren += 1
        return numChildren

    def deleteNode(self, node):
        """
        Delete the node from the tree
        :param node: BSTNode containing the MT
        :return:true if delete is successful, else false
        """

        returnVal = False
        if node is None or node is False:
            '''There is nothing in the tree or not found'''
            print("Failed at deleteNode")
        else:
            parent = node.parent
            numChildren = self.children(node)

            if numChildren == 0:
                '''Node is the parent and only element'''
                if parent is not None:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self._root = None
                returnVal = True

            if numChildren == 1:
                '''Parent only has a single child'''
                if node.left is not None:
                    child = node.left
                else:
                    child = node.right
                if parent is not None:
                    if parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    self._root = child
                child.parent = parent
                returnVal = True

            if numChildren == 2:
                '''Parent has two children'''
                minVal = self.min(node.right)
                # if minVal is not None:
                if minVal is not None:
                    node.key = minVal.key
                    self.deleteNode(minVal)
                    returnVal = True
        return returnVal

    def min(self, node):
        """
        Helper function for delete to find the min val
        I dont need this function anymore. I had a bug I
        spent 2 hours trying to fix, because i was using
        self._root instead of node like a dummy
        :param node: BSTnode
        :return: void
        """

        return self._min(node)

    def _min(self, node):
        """
        Another recursive helper function
        :param node: left tree
        :return: value of min child
        """

        if node is not None:
            '''Had one random crash without this'''
            while node.left is not None:
                node = node.left
        return node

    # def delete(self, id):
    #     """
    #     Delete a node from the tree if the id matches
    #     :param id: int of ticket id
    #     :return: true or false if successful
    #     """
    #
    #     temp = self.find(id)
    #     if type(temp) is BSTNode:
    #         if temp.left is None:
    #             self.transplant(temp, temp.right)
    #         elif temp.right is None:
    #             self.transplant(temp, temp.left)
    #         else:
    #             y = self.min(temp.right)
    #             if y.parent != temp:
    #                 self.transplant(y, y.right)
    #                 y.right = temp.right
    #                 y.right.parent = y
    #             self.transplant(temp, y)
    #             y.left = temp.left
    #             y.left.parent = y

    def inOrder(self, node):
        """
        Inorder traversal on the BST
        :return: string of the traversal
        """

        if type(node) is BinarySearchTree:
            node = self._root
        if node is not None:
            self.inOrder(node.left)
            self._walk += f"{str(node.key.ticketID)}, "
            self.inOrder(node.right)

        return self._walk[:-2]

    def postOrder(self, node):
        """
        Post order traversal of the bst
        :param node: bst
        :return: string of traversal
        """

        if type(node) is BinarySearchTree:
            node = self._root
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self._walk += f"{str(node.key.ticketID)}, "
        return self._walk[:-2]

    def preOrder(self, node):
        """
        Preorder traversal of the bst
        :param node:
        :return: string of traversal
        """

        if type(node) is BinarySearchTree:
            node = self._root
        if node is not None:
            self._walk += f"{str(node.key.ticketID)}, "
            self.preOrder(node.left)
            self.preOrder(node.right)
        return self._walk[:-2]

    def traverse(self, mode):
        """
        Traverse the tree specified by the mode given
        :param mode: string of mode
        :return: string of concatenated traversal
        """

        self._walk = ""
        returnStr = ""
        if mode == "in-order":
            returnStr = self.inOrder(self._root)
        if mode == "post-order":
            returnStr = self.postOrder(self._root)
        if mode == "pre-order":
            returnStr = self.preOrder(self._root)

        return returnStr


def main():
    """
    Main yada yada
    :return: void
    """

    bst = BinarySearchTree()

    p = BSTNode(6)
    r = BSTNode(7)
    l = BSTNode(5)
    # ticket2.ticketID = 7
    # ticket3.ticketID = 5
    # print(bst.insert(ticket1))
    # print(bst.insert(ticket2))
    # print(bst.insert(ticket3))
    r8 = MealTicket("r8")
    r8.ticketID = 8
    r5 = MealTicket("5")
    r5.ticketID = 5
    r2 = MealTicket("2")
    r2.ticketID = 2
    r3 = MealTicket("3")
    r3.ticketID = 3
    r4 = MealTicket("4")
    r4.ticketID = 4
    r1 = MealTicket("1")
    r1.ticketID = 1
    r7 = MealTicket("7")
    r7.ticketID = 7
    r6 = MealTicket("6")
    r6.ticketID = 6

    print(bst.insert("r5"))
    print(bst.insert(r2))
    print(bst.insert(r6))
    print(bst.insert(r7))
    print(bst.insert(r1))
    print(bst.insert(r4))
    print(bst.insert(r3))
    print(bst.insert(r8))
    print(bst.traverse("in-order"))
    print(bst.traverse("pre-order"))
    print(bst.traverse("post-order"))
    # print(bst.delete(3))
    # print(bst.children(bst._root.left.right))
    print(bst.find("6"))
    print(bst.delete(4))
    print(bst.delete(2))
    # print(bst.find(4))

    # print(bst.delete(7))
    # print(bst.delete(2))
    # print(bst.delete(6))
    # print(bst.delete(8))

    #
    #
    # print(bst.delete("3"))
    # print(bst.find("2"))
    # print(bst.traverse("in-order"))
    # print(bst.traverse("post-order"))
    # print(bst.traverse("pre-order"))
    # print(f"Find: {bst.find(5)}")
    # t1 = bst.find(5)
    # t2 = bst.find(6)
    # t3 = bst.find(7)
    # print(t1.key.totalCost)
    # print(t2.key.totalCost)
    # print(t3.key.totalCost)
    # print(bst.traverse("in-order"))
    # print(bst.traverse("post-order"))
    # print(bst.traverse("pre-order"))
    # print(bst.find(6).key.ticketID)
    # print(bst.find(7).key.ticketID)
    # print(bst.find(5))
    # bst.in
    # bst.insert(4)
    # bst.insert(6)
    # bst.insert(10)
    # bst.insert(9)
    # bst.insert(11)
    # print(bst.traverse("pre-order"))
    # print(bst.traverse("in-order"))
    # print(bst.traverse("post-order"))
    # bst.deleteValue(5)
    # bst._walk = ""
    # bst.deleteValue(4)
    # bst._walk = ""
    # bst.deleteValue(11)
    # bst._walk = ""
    # bst.deleteValue(9)
    # print(bst.traverse("in-order"))
    # bst._walk = ""
    # bst.deleteValue(6)
    # print(bst.tr(bst))
    # bst._walk = ""
    # # print(p)
    # # print(l)
    # # print(bst._root.right)
    #
    # # print(bst.delete(6))
    # print(bst.min(bst).key)
    # print(bst.inOrder(bst, "in-order"))


if __name__ == "__main__":
    main()

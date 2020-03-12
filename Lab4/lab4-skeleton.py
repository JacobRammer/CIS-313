"""
Author: Jared Hall
Date: 01/24/2020
Description: A good skeleton code to get you started on RB-Trees
"""
from mealticket import *


class Sentinal:
    """This class builds the sentinal nodes and includes some nifty methods"""

    def __init__(self):
        """
        The constructor for the sentinal class
        A Sentinal is basically a place holder node (root and NULL)
        """
        self.key = None
        self.value = None
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.color = "black"

    def isSentinal(self):
        """ This method makes it easy to check if a given node is a sentinal"""
        return True


class RBNode(object):
    """ Description: This is the node class for the Red-Black Tree."""

    def __init__(self, ticket, color="red"):
        """Constructor for the RBNode class"""
        self.key = ticket.ticketID
        self.value = ticket
        self.color = color

        # Build sentinal nodes and set the initial parent
        self.parent = None
        self.leftChild = Sentinal()
        self.rightChild = Sentinal()

    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        returnValue = "Node: {} - Color: {}\n".format(self.key, self.color)
        returnValue += "Parent: {}\n".format(self.parent.key)
        returnValue += "Left Child: {}\n".format(self.leftChild.key)
        returnValue += "Right Child: {}\n".format(self.rightChild.key)
        return returnValue

    def isSentinal(self):
        """makes it easy to check if a node is a sentinal"""
        return False

    def hasLeftChild(self):
        """ This method returns true if the current node has a left child """
        returnValue = False
        if self.leftChild.parent == self and self.leftChild != self:
            if not self.leftChild.isSentinal():
                returnValue = True
        return returnValue

    def hasRightChild(self):
        """ This method returns true|false depending on if the current
            node has a right child or not."""
        returnValue = False
        if self.rightChild.parent == self and self.rightChild != self:
            if not self.rightChild.isSentinal():
                returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """ Returns True if the current node has only one child."""
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)

    def hasBothChildren(self):
        """ Returns True if the current node has both children"""
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """ Returns true if the current node is a leaf node."""
        returnValue = False
        if self.rightChild.isSentinal() and self.leftChild.isSentinal():
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """Returns true if the current node is a left child"""
        return self.parent.leftChild == self

    def isRightChild(self):
        """Returns true if the current node is a right child"""
        return self.parent.rightChild == self


class RedBlackTree:
    """ Skeleton code for the red-black tree"""

    def __init__(self):
        """ The constructor for the red-black tree"""
        self._root = None
        self.size = 0
        self.output = ""

        # All leaf nodes point to self.sentinel, rather than 'None'
        # Parent of root should also be self.sentinel
        self.sentinel = Sentinal()
        self.sentinel.parent = self.sentinel
        self.sentinel.leftChild = self.sentinel
        self.sentinel.rightChild = self.sentinel

    def traverse(self, mode):
        """The traverse method returns a string rep of the tree according to
           the specified mode
        """
        self.output = ""
        if type(mode) == str:
            if mode == "in-order":
                self.inorder(self._root)
            elif mode == "pre-order":
                self.preorder(self._root)
            elif mode == "post-order":
                self.postorder(self._root)
        else:
            self.output = "  "
        return self.output[:-2]

    def inorder(self, node):
        """ computes the preorder traversal """
        if node.key is not None:
            self.inorder(node.leftChild)
            self.output += str(node.key) + ", "
            self.inorder(node.rightChild)

    def preorder(self, node):
        """computes the pre-order traversal"""
        if node.key is not None:
            self.output += str(node.key) + ", "
            self.preorder(node.leftChild)
            self.inorder(node.rightChild)

    def postorder(self, node):
        """ compute postorder traversal"""
        if node.key is not None:
            self.postorder(node.leftChild)
            self.postorder(node.rightChild)
            self.output += str(node.key) + ", "

    def findSuccessor(self, node):
        """
        This method returns the sucessor of a given node.
        """
        successor = None
        # if node has a right child
        if node.hasRightChild():
            # then successor is the min of the right subtree
            currentNode = node.rightChild
            while currentNode.hasLeftChild():
                currentNode = currentNode.leftChild
            successor = currentNode
        elif node.parent:  # node has no right child, but has a parent
            if node.isLeftChild():  # node is a left child
                successor = self.parent  # then succ is the parent
            else:  # node is right child, and has not right child
                # remove parent's rightChild reference
                node.parent.rightChild = None
                # recursively find call findSuccessor on parent
                successor = self.findSuccessor(node.parent)
                # replace parent's rightChild reference
                node.parent.rightChild = node
        return successor

    # =========================== Mandatory Methods ============================
    # You write these.
    def find(self, ticketID):
        """ Hints: This method returns either a stored mealticket or False
                   just like in the BST lab. Start at the root then make
                   your way to the RBNode whose ticketID matches the input.
                   Then return the value of that node.
        """
        # create your return var
        # start at root
        # while ticketID != currentNode.key
        #    go eiter right or left depending on comparison.
        #    e.g. currentNode.key > ticketID -> curentNode = cn.left or cn.right
        #    break when you hit a sentinal
        # return either false or currentnode.value
        pass

    def delete(self, key):
        """ The delete method starts out the same as BST but then you need
            to restructure your RBT.
        """
        pass

    def insert(self, key):
        """
        Hints: add a key to the tree. Don't forget to fix up the tree
        and balance the nodes.
        """
        pass

    def leftRotate(self, x):
        """ perform a left rotation from a given node"""

        # todo may need to change x.isSentinal back to self.none
        y = x.right
        x.right = y.left

        if y.left is not x.isSentinal():
            y.left.parent = x
        y.parent = x.parent
        if x.parent is x.isSentinal():
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.p = y

    def rightRotate(self, x):
        """ perform a right rotation from a given node"""

        y = x.left
        x.left = y.right
        if y.right is not x.isSentinal():
            y.right.parent = x
        y.parent = x.parent
        if x.parent is x.isSentinal():
            self._root = y
        elif x == x.parent.right:
            x.p.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # ========================== Additional Methods ============================
    # I think these are useful. Implement them if you want.
    def findNode(self, ticketID):
        """
        Hints: This method finds a node and returns it or
               false if no node is found. First do a BST search for the RBNode
               with the same key as the input ticketID. Then return that node.
        """
        # similar to find but returns a node (used internally for find sucessor
        # and delete). Same steps as above, just return currentNode
        pass

    def insertFixup(self, currentNode):
        """Hint: write a function to balance your tree after inserting"""
        pass

    def deleteFixup(self, currentNode):
        """
        Hint: receives a node and fixes up the tree,
              balancing from that node.
        """
        pass


def main():
    """
    Main function for RB tree
    :return: void
    """

    print(ticket1.ticketID)

if __name__ == "__main__":
    # Write a main to test your code. Share on Piazza if you wanna ^,^
    main()

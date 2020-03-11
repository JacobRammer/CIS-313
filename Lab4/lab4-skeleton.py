"""
Author: Sam Peters
Description: Main that checks if your tree maintains RBTree properties
Notes:
The most useful part of this file is the verify_RB_properties() function
which checks all 4 of the properties red black trees have.

This is based off of Jared's skeleton code, if you don't have Sentinal nodes in your tree,
your regular or Sentinal nodes don't have the isSentinal() method, or if your node class has child
attributes named something other than leftChild and rightChild, you'll have to modify this code.
"""

from mealticket import *
from YOURLABFILENAME import *
import random


def random_insert(tree, values):
    """
    Inserts list of values in random order into the tree
    """
    shuffled_values = values.copy() # shuffle values
    random.shuffle(shuffled_values)
    for val in shuffled_values:
        # Creating mealticket with a ticketname of "val" and a ticketID of val
        ticket = MealTicket(str(val))
        ticket.ticketID = val
        status = tree.insert(ticket)
        # if insert fails
        if not status:
            print(f"Insert of {val} failed")

def random_find_delete(tree, values):
    """
    Finds and deletes list of values from tree in random order
    """
    shuffled_values = values.copy()
    random.shuffle(shuffled_values)
    for val in shuffled_values:
        # Tries to call find() method to find a specific ticket
        ticket = tree.find(val)
        if type(ticket) is not MealTicket:
            print(f"Find method did not return a mealticket when called with value {val}")
        # Checking to see if the correct ticket was returned
        elif str(val) != ticket.TicketName:
            print(f"Find method returned wrong mealticket when searching for {val}")

        # Tries to call delete() method to delete a specific ticket
        status = tree.delete(val)
        if not status:
            print(f"Delete of {val} failed")

def verify_RB_properties(tree):
    """
    Tests to make sure that a given tree has the following properties:
    1. The root node is black
    2. No red node has a red parent
    3. Every path from a node to its descendant Sentinal/Null nodes has the same
    number of black nodes along the way
    4. Every node has a .color attribute that is either "red" or "black"
    """
    # Checking if every node has a red or black attribute, comment this out if
    # You're sure your tree does
    if not test_colors(tree._root):
        print("Tree did not meet 4th property")

    # Checking if root node is black
    elif tree._root.color != "black":
        print("Tree did not meet 1st property")

    # Checking if tree obeys second property
    elif not test_redred(tree._root):
        print("Tree did not meet second property")
    # Checking to see if tree obeys 3rd property
    elif not test_blackheight(tree._root):
        print("Tree does not meet third property")

def test_colors(node):
    """ Recursively checks if every node has a color attribute """
    # Shorter names for child nodes
    l_child = node.leftChild
    r_child = node.rightChild
    # Checking if each node has the color attribute and that it's either "red" or "black"
    node_has_color = hasattr(node, "color") and (node.color == "red" or node.color == "black")

    # Recursively calling test_colors() on children if they aren't sentinals
    l_has_color = test_colors(l_child) if not l_child.isSentinal() else True
    r_has_color = test_colors(r_child) if not r_child.isSentinal() else True
    return node_has_color and l_has_color and r_has_color

def test_redred(node):
    """ Recursively checks that no red node has a red parent """
    if node.color == "red":
        if node.parent.color == "red":
            return False
    if node.isSentinal():
        return True
    else:
        return test_colors(node.leftChild) and test_colors(node.rightChild)

def test_blackheight(node):
    """ Recursively checks blackheight property
    Returns either False if something violated the property, or the number of
    black nodes in one path from the current node to the bottom"""
    node_value = 1 if node.color == "black" else 0
    # Checking if we hit the bottom
    if node.isSentinal():
        return node_value
    # Getting the number of nodes in left and right subtrees
    left_subtree = test_blackheight(node.leftChild)
    right_subtree = test_blackheight(node.rightChild)

    # Checking if either subtree has a violation
    if left_subtree is False or right_subtree is False:
        return False
    # Checking if the number of black nodes in paths to the bottom match up
    elif left_subtree != right_subtree:
        return False
    else:
        return node_value + left_subtree



def main():
    """ Main function that runs all the other functions """

    values = [i for i in range(100)]
    tree = RedBlackTree()
    """ COMMENT OUT EVERYTHING BELOW IF YOU HAVEN'T FINISHED INSERT YET """
    print("Testing insert")
    # Testing insertion to see if anything breaks, inserts 100 numbers in random order
    random_insert(tree, values)
    # Checking if tree still has RB properties after inserting 100 numbers in random order
    verify_RB_properties(tree)

    """ COMMENT OUT EVERYTHING BELOW IF YOU HAVEN'T FINISHED FIND OR DELETE YET """
    print("Testing find and delete methods")
    # Randomly removes half of the nodes
    halfof_values = values[:len(values)//2]
    random_find_delete(tree, halfof_values)
    # Verifying rbtree properties are still intact
    verify_RB_properties(tree)

    # Repeating the process for the other 50 nodes
    other_values = values[len(values)//2:]
    random_find_delete(tree, other_values)
    verify_RB_properties(tree)

    # At this point your tree should be empty, maybe add a check to see if that's true


if __name__ == "__main__":
    main()
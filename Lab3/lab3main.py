""" Simple test class for Lab 3 """

from random import randint, shuffle
from mealticket import *
from jrammer_lab3 import *


def generateMealTickets(size):
    """ Generates an array of mealtickets based on the integer <size> """
    mealtickets = []
    for i in range(size):
        ticket = MealTicket("Jared's Meal " + str(i))
        ticket.addItem(("Item 1", round(uniform(0, 30), 2)))
        ticket.addItem(("Item 2", round(uniform(0, 30), 2)))
        ticket.addItem(("Item 3", round(uniform(0, 30), 2)))
        mealtickets.append(ticket)

    # randomize the list of tickets
    IDs = {}
    for ticket in mealtickets:
        newID = randint(1, size)
        while newID in IDs:
            newID = randint(1, size)
        IDs[newID] = newID
        ticket.ticketID = newID
    return mealtickets


def main():
    size = 8
    bst = BinarySearchTree()
    tickets = generateMealTickets(size)

    print("=== Testing Binary Search Tree ===")
    print("Test 1: Inserting tickets")
    for ticket in tickets:
        print("Result", str(ticket.ticketID) + ":", bst.insert(ticket))
    print()

    print("Test 2: Traversals")

    print("In-order:", bst.traverse("in-order"))
    print("Pre-order:", bst.traverse("pre-order"))
    print("Post-order:", bst.traverse("post-order"))
    print()

    print("Test 3: Deleting tickets")
    # generate a list of random ids of random length
    ids = [i for i in range(1, size + 1)]
    shuffle(ids)
    # change the below line if you want to delete a certain number of nodes
    length = randint(1, size)
    ids = ids[:length]  # shorten list to random length 1..size
    print(bst._search(5))
    for i in ids:
        res = bst.delete(i)
        print("Remove", str(i) + ":", res)
    print()

    print("Test 4: Traversals Revisited")

    print("In-order:", bst.traverse("in-order"))
    print("Pre-order:", bst.traverse("pre-order"))
    print("Post-order:", bst.traverse("post-order"))
    print(bst._search(5))

    return


if __name__ == "__main__":
    main()
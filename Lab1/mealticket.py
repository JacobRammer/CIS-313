"""
Author: Jared Hall
Description: A simple meal ticket program.
Date: 01/14/2020
Notes:
    1. This program contains the meal ticket class developed in the video tutorial.
"""
from random import uniform


class MealTicket():
    """ A simple meal ticket class. """
    ID = 1

    def __init__(self, ticketName):
        """ Constructor for the meal ticket class """
        self.TicketName = ticketName
        self.ticketID = MealTicket.ID
        self.totalCost = 0
        self.items = []
        MealTicket.ID += 1

    def addItem(self, item):
        self.items.append(item)
        self.totalCost += item[1]  # tuple 2nd pos is price
        return True

    def display(self):
        print("=== Displaying Ticket ===")
        print("Ticket Name: ", self.TicketName)
        print("Ticket ID: ", self.ticketID)
        print("Total Cost: ", round(self.totalCost, 2))
        print("Ticket Items: ")
        for i in range(0, len(self.items)):
            print("  Item name: ", self.items[i][0], " -- Item cost: ",
                  self.items[i][1])
        print("========== End ==========\n")


ticket1 = MealTicket("Jared's Breakfast")
ticket1.addItem(("Eggs", 4.50))  # adding items as a tuple
ticket1.addItem(("Bacon", 2.50))
ticket1.addItem(("OJ", 1.00))
ticket2 = MealTicket("Jared's Lunch")
ticket2.addItem(("Steak", 14.99))
ticket2.addItem(("Salad", 3.00))
ticket2.addItem(("Lychee", 0.50))
ticket3 = MealTicket("Jared's Dinner")
ticket3.addItem(("Noodles", 11.50))
ticket3.addItem(("Dumplings", 5.99))
ticket3.addItem(("Whiskey", 19.99))
ticket4 = MealTicket("Jared's Snacks")
ticket4.addItem(("Dragon Fruit", 8.50))
ticket4.addItem(("Strawberry", 3.25))
ticket4.addItem(("Passion Fruit", 4.50))

import pprint


# added a function that outputs an array of mealtickets so we gots mo data
def generateMealTickets(size):
    """ Generates an array of mealtickets based on the integer <size> """
    mealtickets = []
    vals = [33.45, 45.82, 36.87, 43.88, 40.09, 20.6, 30.07, 28.99]
    for i in range(size):
        ticket = MealTicket("Jared's Meal " + str(i))
        ticket.addItem(("Item 1", float(vals[i]), 2))
        mealtickets.append(ticket)
    return mealtickets


if (__name__ == "__main__"):
    def main():
        print(" === Testing MealTicket class ===")

        # Step-03: Display tickets
        ticket1.display()
        # ticket2.display()
        # ticket3.display()
        # ticket4.display()

        return True


    main()

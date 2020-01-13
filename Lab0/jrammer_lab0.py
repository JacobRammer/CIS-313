"""
Jacob Rammer
Lab 0
"""


class FibSequence:
    """
    Calculate Fibonacci Numbers
    """

    def __init__(self):
        self.array = [0, 1]
        self.fib_num = 0
        self.ord_indicator = ""

    def compute(self, n: int):
        """
        Method to calculate the fibonacci sequence by appending
        to a list.
        :param n: what is the nth fibonacci number
        :return: void
        """

        for i in range(n):
            self.array.append(self.array[i] + self.array[i + 1])
        self.fib_num = self.array[n - 1]
        self.display_message(n)

    def display_message(self, n: int):
        """
        Dynamically updates the ordinal indicator to the proper
        format. 1st, 2nd, 3rd etc
        Reverse number as the ordinal indicator is based of the
        last digit.
        :param n: nth Fibonacci number
        :return: void
        """

        temp_val = str(n)  # cast n to str to keep ifs cleaner

        if 10 < int(temp_val) < 20:  # teens are a special case and only ones I can think of
            self.ord_indicator = "th"
        elif temp_val[::-1][0] == "1":
            self.ord_indicator = "st"
        elif temp_val[::-1][0] == "2":
            self.ord_indicator = "nd"
        elif temp_val[::-1][0] == "3":
            self.ord_indicator = "rd"
        else:
            self.ord_indicator = "th"


def main():
    """
    Main function. Asks for input and validates input
    :return: void
    """

    while True:
        try:  # try to get valid input
            nth_fib = input("Enter a digit or \'q\' to quit: ").lower()
            if len(nth_fib) == 0:
                print("Please enter a positive integer or \'q\'\n")
                main()
            if nth_fib == "q":
                exit()
            nth_fib = int(nth_fib)
            if int(nth_fib) > 0:
                fib_num = FibSequence()
                fib_num.compute(int(nth_fib))
                print(f"The {nth_fib}{fib_num.ord_indicator} Fibonacci number is: {fib_num.fib_num}\n")
            else:
                print("Please enter a positive integer or \'q\'\n")
        except ValueError:  # if non-valid input is entered, don't crash
            print("Please enter a positive integer or \'q\'\n")


if __name__ == "__main__":
    main()

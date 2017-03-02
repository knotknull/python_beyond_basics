#!/usr/bin/python3.5
from pprint import pprint as pp
# Class : define structure and behaviour of object
#         Class controls initialization
#
# class keyword to define a class and class name by convention is CamelCase
# class is a statement that can occur anywhere an binds a class definition
# to a class name
# Everything is an object in python, including the classes
#
#   Method:          a function defined within a class
#   Instance method: functions which can be called on objects
#   self :           first argument to all instance methods

#   Instance method:        f.number()
#   also Instance method:   Flight.number.number(f)
#
#   __init__(self):   initialization method for initializing new objects
#                 :   __init__(self) is NOT a constructor
#                 :   no return, just initilizes self
#                 :   self is similar to this in Java
#
#  Class Invariants: Truth about an object that endures for its lifetime


class Flight:
    """A flight with a particular passengar aircraft."""
    # pass    # simplest do nothing class as empty blocks not allowed

    # instance method for initializing new objects
    def __init__(self, number, aircraft):
        # Class Invariant checks, proper format of Flight number
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("No airline code in '{}'".format(number))

        self._number = number    # convention _var are implementation details
        self._aircraft = aircraft

        # initialize seating plan over rows, seats. Initialize to None
        # a '\' is used to split the line because there is no open ( or {
        # to allow a line split without a '\'
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
            [{letter: None for letter in seats} for _ in rows]

    def number(self):           # This is an instance method
        return self._number     # everything is a public in a class

    def airline(self):           # This is an instance method
        return self._number[:2]  # get airline code

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """ Parse a seat disgnator into a valid row and letter.

        Args:
          seat: A seat designator such as '12C' or '21F'.

        Returns:
          A tuple containing an integer and a string for row and seat
        """
        rows, seat_letters = self._aircraft.seating_plan()

        # the the letter of the seat by taking end of list index [-1]
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        # get the "text" of the row number, slice from start to before end
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        # now check if the row is actually in the rows of the seating plan
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """ Allocate a seat to a passenger.

        Args:
          seat: A seat designator such as '12C' or '21F'.
          passenger: The passenger name.

        Raises:
          ValueError: If the seat is unavailable.
        """

        row, letter = self._parse_seat(seat)

        # Check if someone is already in that seat
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied.".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """ Relocate a passenger to a different seat.

        Args:
          from_seat: The existing seat designator for the passenger to be moved

          to_seat: The new seat designator.
         """
        # Check if anyone in from_seat
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(
                "No passenger to relocate in {}".format(from_seat))

        # Check if anyone in to_seat
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        # Relocate seat
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    # Holy crap look at this code:
    # Two nested generator expressions
    # "Outer Expression" i.e. lines 2 and 3 filters all rows that are not None
    # "Inner Expression" i.e. line 1 sums up all None values in that row
    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating  # returns not None rows i.e.
                   if row is not None)       # skips very first unused row


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

        # Here we go this is going to be fun
        # this returns a tupl of range(1, num_rows) and a
        # string or alphas, one for each num_seats per row
        # i.e.  (range(1,15), 'ABCDEF')
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


def make_flight():
    f = Flight("AA1225",
               Aircraft("XPy1", "PyAir 220", num_rows=22, num_seats_per_row=6))
    f.allocate_seat('13D', 'Father Guido Sarducci')
    f.allocate_seat('5F', 'Pope John')
    # f.allocate_seat('5F', 'The Devil')
    f.allocate_seat('20A', 'Mr. Buddha')
    f.allocate_seat('19B', 'Sonny Bono')

    return f


# this is a 'Flight' object
f = make_flight()
print("type(f) = {}".format(type(f)))
print ("f.number()  = ", f.number())
print ("f.airline() = ", f.airline())
print("aircraft.model = ", f.aircraft_model())
print("f.seating_plan = ")
pp(f._seating)

# Move Buddha next to the Pope
print ("Number of available seats {}".format(f.num_available_seats()))
f.relocate_passenger("20A", "5E")
f.allocate_seat("1A", "Mike-D")
f.allocate_seat("1E", "Kid Ad-Rock")
print ("Number of available seats {}".format(f.num_available_seats()))
pp(f._seating)


# acraft = Aircraft(registration="X-Py1", model="Pythair 220",
#                   num_rows=22, num_seats_per_row=6)
# print("aircraft.registration = ", acraft.registration())

# NOTE: Law of Demeter:  The principle of least knowledge.
#       Never call methods on objects you receive from other calls...
#       or  Only talks to your friends


##
# This is the Seating Data structure
# -  all rows are in a list (zero element not used representing 1-based)
# -  each element in row has a dict of seat (k="A") to passenger(v="Bob")
##
# rows, seats = self._aircraft.seating_plan
# self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
#                    ^     ^       ^
#            /-------|     |       |
#            |             |       Dictionary comprehension which takes
#        Zeroth row = None |       a letter in seats and creates k, v of
#                          |       k=Seat Letter, v=None (initialization)
#                          |
#                          Listcomprehension creating an entry for each row
#                          this is iterated via for _ in rows
#                          NOTE: _ is used because don't need row number
##

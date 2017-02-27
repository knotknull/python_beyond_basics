#!/usr/bin/python3.5

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
    # pass    # simplest do nothing class as empty blocks not allowed

    def __init__(self, number):  # instance method for initializing new objects
        # Class Invariant checks, proper format of Flight number
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("No airline code in '{}'".format(number))

        self._number = number    # convention _var are implementation details

    def number(self):           # This is an instance method
        return self._number     # everything is a public in a class

    def airline(self):           # This is an instance method
        return self._number[:2]  # get airline code

# this is a 'class' object
print("type(Flight) = {}".format(type(Flight)))

f = Flight("AA1225")
# this is a 'Flight' object
print("type(f) = {}".format(type(f)))
print ("f.number()  = ", f.number())
print ("f.airline() = ", f.airline())

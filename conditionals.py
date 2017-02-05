#!/usr/bin/python3.5

# if expr: << expr converted to boolean

if True:
    print("This is True")

if False:
    print("Not going to print this but ...")
else:
    print("This is False")


# elif expr: << combined else if  (Flat is better than nexted !!)

## NOT Preferred
h=42
if h > 50:
    print("greather than 50")
else:
    if h < 20:
        print("Less than 20")
    else:
        print("between 20 and 50")

## PREFERRED
if h > 50:
    print("greather than 50")
elif h < 20:
        print("Less than 20")
else:
    print("between 20 and 50")

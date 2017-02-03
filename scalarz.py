#!/usr/bin/python3.5

# scalar types:
# int -- arbitrary precision integer
# float -- 64 bit floating point number
# NoneType = None = the null object
# bool = True | False : boolean logic values

tenint = 10
roundint = int(10.2)
binint = 0b10
octint = 0o10
hexint = 0x10
print("Here are the ints:")
print(tenint)
print(roundint)
print(binint)
print(octint)
print(hexint)


# Float info: IEEE-754 double prec(64-bit)
#             53 bits of binary precision
#             15 to 16 bits of decimal precision
threefloat = 3.25
eeefloat = 3e8
smalle_float = 1.616e-35
nanfloat = float("nan")  # Not a Number
posinfloat = float("inf")
neginfloat = float("-inf")
print("\n\nHere are the floats:")
print(threefloat)
print(eeefloat)
print(smalle_float)
print(nanfloat)
print(posinfloat)
print(neginfloat)


# here is null values
print("Here is the NoneType")
a = None
print(a is None)

# here are the bool types
print("Here is the bool Type")
print(True)    # !0 considered "truth"
print(False)   # 0 considered "falsey"
print(bool(0))
print(bool(42))
print(bool([]))          # empty collections considered falsey
print(bool([1, 5, 10]))  # non-empty collections considered truthy
print(bool(""))          # empty strings considered falsey
print(bool("stringy"))   # non-empty string considered truthy

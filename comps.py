#!/usr/bin/env python3.5
from math import factorial
from pprint import pprint as pp

# Comprehensions: concise syntax describing
#                 - lists
#                 - sets
#                 - dictionaries
#    declaritive / functional style: readable, expressive, effective

# list Comprehension
words = "Hickory Dickory Dock the Mouse ran up the clock or something".split()
print("words = ", words)

# here comes the Comprehension:
# declared with brackets like a list but contains "delarative code" which
# describes how the is created
print("compre = [len(word) for word in words]")
compre = [len(word) for word in words]
print("compre = ", compre)

#  generic form: [ expr(item) for item in iterable ]
# This is the same
#      comps = [len(word) for word in words]
# as this:
#      comps = []
#      for word in words:
#          comps.append(len(word))

fibs = [len(str(factorial(x))) for x in range(20)]  # Any iterable
print("fibs", fibs)

# set Comprehension, same thing except uses {} instead of []
# Since it is a set, duplicates are removed
fibset = {len(str(factorial(x))) for x in range(20)}  # Any iterable
print("fibset", fibset)

# dictionary Comprehension:
# { key_expr:val_expr for item in iterable }
# NOTE: item from iterable returns two values: key_expr, val_expr

# setup dictionary
country_to_capital = {'United Kingdong': 'London',
                      'Brazil': 'Brazilia',
                      'Morocco': 'Rabat',
                      'Sweden': 'Stockholm'
                      }
# Now setup the dictionary Comprehensions: reverse lookup being done
# NOTE: dictionary.items() returns the key, value tuple which is unpacked
#       to country, capital  and then saved as key=capital, val=country
capital_to_country = {capital: country for country,
                      capital in country_to_capital.items()}
print("country_to_capital: ")
pp(country_to_capital)
print("capital_to_country: ")
pp(capital_to_country)

# If comprehension creates duplicate keys then
# later keys overwrite earlier keys

# create a list
wrdlst = ["hi", "hello", 'foxtrod', 'hotel']
keycmp = {x[0]: x for x in wrdlst}
print("wrdlst = ")
pp(wrdlst)
print("keycmp = ")
pp(keycmp)

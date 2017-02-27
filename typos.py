#!/usr/bin/env python3.5
from pprint import pprint as pp

# print types


def xtype(x):                # for loops based on this logic
    print("x = {}".format(x))
    print("type(x) = {}".format(type(x)))

x = 5
xtype(x)  # int

x = 3.15
xtype(x)  # float

x = "hi"
xtype(x)  # str

x = [1, 2, 3]
xtype(x)  # list

x = (1, 2, 3)
xtype(x)  # tupl

x = {1, 2, 3}
xtype(x)  # set

x = {'one': 1, 'two': 2, 'three': 3}
xtype(x)  # dictionary

x = [z for z in [1, 2, 3]]
xtype(x)  # generator or list comp

x = {z for z in [1, 2, 3]}
xtype(x)  # generator or set comp

x = (z * z for x in range(1, 1000001))
xtype(x)  # comp generator


# x = {a: b for idx, val in {'one': 1, 'two': 2, 'three': 3}.items()}
# xtype(x)  # generator or dictionary comp

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
xtype(capital_to_country)  # comp generator

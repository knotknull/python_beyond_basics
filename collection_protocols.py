#!/usr/bin/env python3.5
from pprint import pprint as pp  # import pprint func from pprint module

# Protocol          Implementing Collections
# --------          ------------------------------------
# Container         str, list, range, tuple, bytes, set, dict
# Sized             str, list, range, tuple, bytes, set, dict
# Iterable          str, list, range, tuple, bytes, set, dict
# Sequence          str, list, range, tuple, bytes
# Mutable Sequence  list
# Mutable Set       set
# Mutable Mapping   dict

# To implement a protocol, objects must support certain operations

# Protocol          Operations
# --------          ------------------------------------
# Container         membership testing: in, not in
# Sized             determine number of elements with len(collection)
# Iterable          produce an iterator w/ iter(s), can be used in for loops
# Sequence          retrieve elements by index: item = seq[index]
#                   find items by value:        index = seq.index(item)
#                   count items :               num = seq.count(item)
#                   produce reversed sequence:  rev = reversed(seq)

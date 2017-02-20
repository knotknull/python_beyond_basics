#!/usr/bin/python3.5
from pprint import pprint as pp  # import pprint func from pprint module

# dict : mutable mappings of keys to values
#      : unordered mapping from unique, immutable keys to mutable values
#      : keys MUST be immutable (str, numbers, tuples ok   NO lists)
#      : i.e.    lookup['key']   = 0    ok
#      :         lookup[5]       = 0    ok
#      :         lookup[(1,2,3)] = 0    ok
#      :         lookup[[1,2,3]] = 0    NOT ok
#
#  Order is arbitrary!!

# literal dictionary
name_nums = {'joe': 5,
             'bob': 12,
             'infy': float("inf"),
             }

print("bob = ", name_nums['bob'])
print("infy = ", name_nums['infy'])

# use dict() to create a dictionary from name value tuples
name_age = [('fred', 2), ('alice', 3), ('sam', 14), ('bob', 1), ('norm', 5)]
namage = dict(name_age)
print ("name_age [] = ", name_age)
print ("namage   {} = ", namage)

# can create a dictionary by calling dict with keywords
colores = dict(red='rojo', blue='azul', black='negro', listo=[0, 1, 2])
print ("colores {} = ", colores)

# dict copying is shallow, two ways to copy a dictionary
# via dict.copy() or dict(x)
d = colores.copy()
e = dict(d)
print ("d {} = ", d)
print ("e {} = ", e)

# update colores['listo'], append the list that is at 'listo'
colores['listo'].append(3)
colores['listo'] += [4]
colores['listo'].append(5)
print("update color >>  colores['listo'].append(3) ...")
print ("colores {} = ", colores)
print ("d {} = ", d)  # because of shallow copy, d and e are updated to
print ("e {} = ", e)

# extend / update a dictionary with another dictionary
temp = dict(white='blanco', orange='naranja', yellow='amarillo')
d.update(temp)
print("temp = ", temp)
print("d    = ", d)
print("e    = ", e)

# iterate over keys
for key in d:
    print("{k} => {v}".format(k=key, v=d[key]))

print("iterate values only")
# iterate over values only via values()
for val in d.values():
    print("val = {v}".format(v=val))

print("iterate keys only")
# iterate over keys only via keys()
for key in colores.keys():
    print("key = {k}".format(k=key))

print("iterate key, value (tuple)")
# use items for iterable view returning key-value tuples
for k, v in d.items():
    print("{key} => {val}".format(key=k, val=v))

# membership test, via keys only
print("membership test: in / not in (keys only)")
print("purple in colores: ", 'purple' in colores)
print("red    in colores: ", 'red' in colores)
print("rojo   in colores: ", 'rojo' in colores)

# delete a dictionary entry
print("before del d:", d)
del d['white']
print("before del d:", d)

# pretty print dictionary
print ("pp(d):")
pp(d)

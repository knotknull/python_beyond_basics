#!/usr/bin/python3.5

# list : heterogeneous mutable sequences of bytes

# get a list from split
s = "eenie meenie minie moe piggie . .. ...".split()
print(s)

# use a negative index to get piggie
# -8     -7    -6    -5   -4    -3 -2 -1
# "eenie meenie minie moe piggie .  .. ..."
print("s[-4] = {}".format(s[-4]))

# NOTE: 0 == -0
print("what is s[0]  = {}".format(s[0]))
print("what is s[-0] = {}".format(s[-0]))

# Let's slice it up, positive and negative indexes
print("s[1:4] = {}".format(s[1:4]))
print("s[1:-1] = {}".format(s[1:-1]))

# start and stop indexes are optional
print("s[3:] = {}".format(s[3:]))   # from 3 to end of list
print("s[:3] = {}".format(s[:3]))   # from start to 2

# no indexes used for copying (shallow copy)
# shallow copy = new list with same obj references as source list
# NOTE: could also copy like copy=s.copy() or copy=list(s)

s.append([0, "list"])
copy = s[:]

print("copy = {}".format(copy))
print("s    = {}".format(s))
print("copy == s   {}".format(copy == s))
print("copy is s   {}".format(copy is s))

# example of shallow copy: lets change the list at the end of s and see what
# happens to the list at the end of copy
print("s[-1].append(5)  # appending to list in s also affect list in copy")
s[-1].append(5)          # appending to list in s also affect list in copy
print("s    = {}".format(s))
print("copy = {}".format(copy))

# list repetition
rep = [5, 10]
print("rep={}  rep*3={}".format(rep, rep * 3))

# list repetition is used to initialize a known quantity to an initila value
# NOTE: repetition is shallow
bigrep = [0] * 9
for idx, val in enumerate(bigrep):
    print("idx={}  val={}".format(idx, val))

# find an item using index
print(" moe is at {}".format(s.index('moe')))
# print(" ziggy is at {}".format(s.index('ziggy'))) # Give ValueError

# get count and check for membership
print ("moe count = {}".format(s.count('moe')))
print (". in s = {}".format('.' in s))
print ("~ in s = {}".format('~' in s))

# delete using del or remove
goody = "All Good Boys Do Fine".split()
print(goody)
del goody[-1]
print(goody)
goody.remove('Do')
print(goody)

# Now insert
goody.insert(0, 'Maybe')
print(goody)

# Add to list with += or append
goody += ['Do']
print(goody)
goody.extend(['Fine'])
print(goody)

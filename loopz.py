#!/usr/bin/python3.5

# while expr: << expr converted to boolean

x = 10

while x > 0:
    print (x)
    x -= 1


# break : << jumps out of loop (inner most)
while True:     # infinite loop
    response = input()
    if int(response) % 7 == 0:
        break

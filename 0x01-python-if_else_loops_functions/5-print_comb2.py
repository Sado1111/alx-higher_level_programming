#!/usr/bin/python3
"""
prints numbers from 0 to 99
Numbers must be separated by ,, followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 2 print functions with string format
You can only use one loop in your code
"""

for x in range(10):
    for y in range(10):
        print('{}{}'.format(x, y), end='' if x == 9 and y == 9 else ', ')
print()

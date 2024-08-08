#!/usr/bin/python3
"""
Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 3 print functions with string format
You can only use no more than 2 loops in your code
"""

for i in range(8):
    for j in range(i + 1, 10):
        print('{}{}'.format(i, j), end=', ')
print(f'89')

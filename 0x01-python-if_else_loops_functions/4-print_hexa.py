#!/usr/bin/python3
""" program prints numbers  0 to 98 in decimal and in hexadecimal """

for i in range(99):
    print('{:d} = 0x{:x}'.format(i, i))

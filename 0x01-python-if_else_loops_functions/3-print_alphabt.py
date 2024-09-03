#!/usr/bin/python3
""" program prints the ASCII alphabet (except q and e) in lowercase."""
for i in range(97, 123):
    if i != ord('q') and i != ord('e'):
        print('{}'.format(chr(i)i), end='')

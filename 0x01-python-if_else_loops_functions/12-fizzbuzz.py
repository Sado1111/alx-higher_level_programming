#!/usr/bin/python3

"""
function that prints the numbers from 1 to 100 separated by a space.
For multiples of three print Fizz instead of the number and for
    multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.
Prototype: def fizzbuzz():
Each element should be followed by a space
You are not allowed to import any module

"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ' if i != 100)
        else:
            print('{}'.format(i), end=' ')
    print()

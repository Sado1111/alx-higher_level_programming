#!/usr/bin/python3

"""
Function that returns a tuple with the length of a
  string and its first character.
    Prototype: def multiple_returns(sentence):
    If the sentence is empty, the first character should be equal to None
    You are not allowed to import any module
"""


def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])

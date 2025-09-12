#!/usr/bin/python3
"""
This is the "text_indentation" module.

The text_indentation module supplies one function,
text_indentation().  For example,

>>> text_indentation("Indent. This: Text?)
    Indent.

    This:

    Text?

"""


def text_indentation(text):
    """
    Print text with 2 new lines after
    the '.', '?', and ':' characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    ignoreSpace = 0
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
            ignoreSpace = 1
        elif ignoreSpace and char == ' ':
            ignoreSpace = 0
        else:
            print(char, end="")

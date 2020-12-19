# -*- coding: utf-8 -*-
"""
Problem No: 12 (Text Wrap)

"You are given a string  and width .
Your task is to wrap the string into a paragraph of width ."

Example:
    
"Input:
String: ABCDEFGHIJKLIMNOQRSTUVWXYZ
width:4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ"


"""
import textwrap

# function for textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    # Take inputs from user
    string, max_width = input("Enter your text here: "), int(input("Enter your max_width: "))
    # store the result in variable
    result = wrap(string, max_width)
    # print the result
    print(result)

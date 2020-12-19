# -*- coding: utf-8 -*-
"""
Problem No: 14 (string format)

"Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order 
specified above for each  from  to . Each value should be 
space-padded to match the width of the binary value of ."

Example:
"Input: 17
Output:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001     "
"""

def print_formatted(number):
    # your code goes here
    l = len("{0:b}".format(number))
    
    for i in range(1, number+1):
        # Justify the width like l
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=l))

if __name__ == '__main__':
    number = int(input("Enter your number: "))
    result = print_formatted(number)
    print(result)
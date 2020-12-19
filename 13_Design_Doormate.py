# -*- coding: utf-8 -*-
"""
Problem No: 13 (Design Doormat)

"Mr. Vincent works in a door mat manufacturing company. 
One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters."

Example:
"Input:  7 21
output : top image in next column


Input: 11 33
output : bottom image in next column"

"""
# take user inputs from the user
rows, columns = map(int, input('Enter Rows and Columns respectively with use of space button: ').split(' '))

# iterate from 1 to number of rows
for i in range(1, rows, 2):
    # alignment the symbol (.|.) in center  
    print((".|."*i).center(columns, '-'))
    
# alignment the WELCOME in center of the doormate
print("WELCOME".center(columns, '-'))

    
for i in range(rows - 2, -1, -2):
    print(('.|.'*i).center(columns, '-'))

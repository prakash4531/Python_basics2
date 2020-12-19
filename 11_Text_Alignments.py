
# -*- coding: utf-8 -*-
"""
Problem No: 11 (Text Alignments)

"User enter the text (0 < len < 20) and alignment (left, center, right). 
print the aligned out put and by adding - to make alignment"

Formula:
-Left:
>>> print 'Praveen'.ljust(width,'-')
Praveen---------- 

-Right
>>> print 'Praveen'.rjust(width,'-')
----------Praveen
-Center

>>> print 'Praveen'.center(width,'-')
-----Praveen-----

Example:
    
Input: 
String: Praveen
Alignment: center
output: -----Praveen-----

"""
string = input('Enter your text here: ')
alignment = input('Enter your alignment here: ')

print("Thea original string is : \n", string, "\n")


width = 20
left = string.ljust(width, '-')
right = string.rjust(width, '-')
center = string.center(width, '-')

if alignment == 'left':
    print(left)
elif alignment == 'right':
    print(right)
elif alignment == 'center':
    print(center)
else:
    print("Please write the alignment input from left,right and center: ")

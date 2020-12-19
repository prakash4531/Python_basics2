# -*- coding: utf-8 -*-
"""
problem No : 9 (String Split and Join)

You are given a string. Split the string on a " " (space)
delimiter and join using a - hyphen.


"""
# Take input from user
string = input('Enter your text here: ')

# split the string
s = string.split(' ')

print(s)

# join the string after split
j = '-'.join(s)

print(j)



#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Jose Andres Ruiz '
__date__ = '16/07/2024'
__proyect__ = 'exercise1.py'
__description__ = ''' This program calculates the sum of the numerical values of the letters in a given name.
 Each letter in the English alphabet is assigned a number from 1 to 26 (A = 1, B = 2, ..., Z = 26). 
 The program ignores non-English letter characters and treats lowercase and uppercase letters equally.'''



def name_to_number(name:str) -> int:
    """
    parameters
    ----------
        :param name : str
                description -> Name of the person
    returns
    -------
        int : The sum of the letters
    """

    # -- Convert name to uppercase
    name = name.upper()

    # -- Initialize sum
    total = 0

    # -- Loop through each character in the name
    for char in name:
        # -- Check if the character is an English letter
        if 'A' <= char <= 'Z':
            # -- Convert character to corresponding number and add to total
            total += ord(char) - ord('A') + 1

    return total

print("What would be the sum of all the letters in your name?")
yourname = input("What is your name? ")
result = name_to_number(yourname)
print(f"The sum of the Letters in your name '{yourname}' is {result}. ")

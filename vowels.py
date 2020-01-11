#!/bin/python3
# vowels .py
# Level: Easy

# Return the number (count) of vowels in the given string.
# a, e, i, o, and u
# The input string will only consist of lower case letters and/or spaces.

# Second iteration - more efficient and less code 

def count2(inputStr):
    num_vowels = 0
    for letter in inputStr:
    	if letter in 'aeiou':
    		num_vowels = num_vowels + 1
    		

    print(num_vowels)
    return num_vowels
	
	
    
count2("abceioua")
print()
count2('aieoulsojdfu')


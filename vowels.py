#!/bin/python3

# Vowels 

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.

# Iteration 1 
# The Dirty Way Out

def getCount(inputStr):
    num_vowels = 0
    for letter in inputStr:
    	if letter == 'a':
    		num_vowels = num_vowels + 1
    	if letter == 'u':
    		num_vowels = num_vowels + 1
    	if letter == 'o':
    		num_vowels = num_vowels + 1
    	if letter == 'i':
    		num_vowels = num_vowels + 1
    	if letter == 'e':
    		num_vowels = num_vowels + 1
    	else:
    		pass

    print(num_vowels)
    return num_vowels
	
	
    
getCount("abceioua")

print()

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


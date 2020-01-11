#!/bin/python3
# exclaim.py

# Remove a exclamation mark from the end of string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
# My attempt
def remove(s):
    if s.endswith('!'):
        print(s[:-1])
        return (s[:-1])
    else:
        print(s)
        return(s)
    

remove("Hi!")
remove("Hi!!!")
remove("!Hi")
remove("Hi! Hi!")
remove("Hi")

# Other users attempts
def remove(s):
    return s[:-1] if s.endswith('!') else s

def remove(s):
    return s[:-1] if s and s[-1] == '!' else s

def remove(s):
    if s.endswith("!"):
        s = s[:-1] 
    return s

#!/bin/python3
# exclaim.py
# Level: Easy

# Remove an exclamation mark from the end of string. Assume that the input data is always a string

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

# Other attempts I found online
def remove(s):
    return s[:-1] if s.endswith('!') else s

def remove(s):
    return s[:-1] if s and s[-1] == '!' else s

def remove(s):
    if s.endswith("!"):
        s = s[:-1] 
    return s

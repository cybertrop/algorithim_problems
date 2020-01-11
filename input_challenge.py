#!/bin/python3
# input_challenge.py
# Level: Easy

"""
Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:

Prompts the user for a message to echo.
Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
Defines a function that takes a message and count then prints the message that many times.
To end the script, call the function with the user-defined values to print to the screen.
"""
# My attempt

def message():
	prompt = input('Please type your message to echo: ')
	prompt_number = input("Please type how many times to print your message: ")
	if prompt_number == '':
		prompt_number = 1
	print((prompt + ' ') * int(prompt_number))
message()

# Other Answers

"""  

message = input("Enter a message: ")
count = input("Number of repeats [1]: ").strip()

if count:
    count = int(count)
else:
    count = 1

def multi_echo(message, count):
    while count > 0:
        print(message)
        count -= 1

multi_echo(message, count)

"""

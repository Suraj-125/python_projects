"""
This is a simple string project where we performed in the basics of string manipulation using function and
switch case statement and stored all the keys in dictionaries.........................
"""

option = input("Enter the case you want to perform : ")
value = input (" Enter the value : ")

''' Defining the function that wanted to peform as a string manipulation '''

def length (value) :
    return len(value)

def uppercase ( value ):
    return value.upper()

def lowercase (value):
    return value.lower()

def splitting (value):
    return value.split()

def stripping (value):
    return value.strip()

def reversing (value):
    return value[::-1]

def invalid (value):
    return "This is invalid"

def switch_statement(option, value):
    switch_dict = {
        "length" : length,
        "upper"  : uppercase,
        "lower"  : lowercase,
        "split"  : splitting,
        "strip"  : stripping,
        "reverse": reversing
    }

    new = switch_dict.get(option, invalid)
    return new(value)

result = switch_statement(option, value)
print(result)




















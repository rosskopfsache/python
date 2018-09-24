#!/usr/bin/python3.6

def get_fibonacci(count):
    '''returns a list with as many fibonacci numbers as defined with the passed integer value'''
    a = 2
    if count < 1:
        result = []
    elif count < 2:
        result = [1]
    elif count < 3:
        result = [1,1]
    elif count >= 3:
        result = [1,1]
        while a < count:
            result.append((result[a-1] + result[a-2]))
            a=a+1
    return result

def get_int(description = "Type in a number: "):
    '''Returns integer value for user input'''
    return int(input(description))

print(get_fibonacci(get_int("Number of Fibonacio numbers?: ")))
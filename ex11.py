#!/usr/bin/python3.6

def get_int(description = "Type in a number: "):
    '''Returns integer value for user input'''
    return int(input(description))

def is_prime(number):
    '''Checks a given integer value if it is a prime and returns true or false'''
    i = 2
    while i < number:
        if number % i == 0:
            return False
            break
        i=i+1
    return True

result = is_prime(get_int("Check number for prime: "))
print(result)
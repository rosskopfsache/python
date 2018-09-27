#!/usr/bin/python3.6

import random
import string
import sys 

def generatePassword(numbers=True, letters=True, special=True, length=16):
    '''
    Randomly generating a password with following input parameters:
        - boolean numbers [default:True]  >  include numbers in password
        - boolean letters [default:True]  >  include letters in password
        - boolean special [default:True]  >  include special characters in password
        - int length [default:16]         >  length of generated password
    '''
    raw = []
    if numbers is True:
        numbers = list(range(length))
        raw = raw + numbers
    if letters is True:
        letters = list(string.ascii_letters)
        raw = raw + letters
    if special is True:
        special = ['!', '#', '+', ',','.','$','&','(',')','?','*']
        raw = raw + special
    random.shuffle(raw)
    pw = ''.join(str(i) for i in raw[:length])
    
    return pw

print(generatePassword(True, True, True, 16))
#!/usr/bin/python3.6

import random

def generatePassword():
    numbers = random.sample(range(1,11),10)
    chars = random.choice('a-Z')
    return chars

print(generatePassword())
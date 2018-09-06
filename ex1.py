#!/usr/bin/python3

import datetime

curYear = datetime.datetime.now().year

name = input("What is your name?: ")
age = int(input("What is your age?: "))
numberOfCopies = int(input("How many cpoies you want?: "))
result = curYear + 100 - age
counter = 1

while counter <= numberOfCopies:
    print(f'Hey {name}, you will get 100 years old in {result}!')
    counter = counter + 1


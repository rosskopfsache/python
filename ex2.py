#!/usr/bin/python3

number = int(input("Tell me a number: "))
if (number % 2) == 0:
    if (number % 4) == 0:
        print("The number is a multiple of 4")
    else:
        print("The number is even")
else:
    print("The number is odd")

num = int(input("Gimme another number: "))
check = int(input("Gimme a divider: "))
if (num % check) == 0:
    print("That devides evenly")
else:
    print("That devides NOT evenly")
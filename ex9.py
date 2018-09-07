#!/usr/bin/python3

import sys
import random

trys = 0
while True:
    number = random.randint(1, 9)
    guess = input("Guess the number within 1 - 9: ")
    if guess == "exit":
        print(f"Exiting - you tried it {trys} times")
        break
    elif int(guess) < number:
        print("Guess too low")
    elif int(guess) > number:
        print("Guess too high")
    elif int(guess) == number:
        print("Exactly right")
    trys = trys + 1
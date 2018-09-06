#!/usr/bin/python3

string = input("Check word for palindrome: ")
stringReverse = string[::-1]
if string == stringReverse:
    print("Its a palindrome!!")
else:
    print("Its NO palindrome!!")
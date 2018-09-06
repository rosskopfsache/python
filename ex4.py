#!/usr/bin/python3

num = int(input("Number?: "))
divisor = num
while divisor != 0:
    if (num % divisor) == 0:
        print(divisor)
    divisor = divisor - 1
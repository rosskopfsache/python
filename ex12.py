#!/usr/bin/python3.6

def get_first_and_last(list):
    '''returns first and last element of a list'''
    lastIndex = len(list) - 1
    firstIndex = 0
    return (list[firstIndex], list[lastIndex])

a = [5, 10, 15, 20, 25]

print(get_first_and_last(a))
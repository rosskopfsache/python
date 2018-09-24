#!/usr/bin/python3.6

def remove_duplicates_set(param):
    '''Function gets a list and returns the given list without duplicates.'''
    result = list(set(param))
    return result
def remove_duplicates_loop(param):
    '''Function gets a list and returns the given list without duplicates using a loop'''
    result = []
    for i in param:
        if i not in result:
            result.append(i)
    return result

print(remove_duplicates_loop([1,1,3,4,5,5,6,5,3,9]))
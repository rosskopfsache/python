#!/usr/bin/python3.6

def change_word_order(words):
    newOrder = words.split()
    newOrder.reverse()
    #newOrder = "-".join(newOrder)
    return newOrder

print(change_word_order("this is a list of words"))
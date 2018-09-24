#!/usr/bin/python3.6

import random

a = random.sample(range(1, 15),10)
b = random.sample(range(1, 15),12)

common = []

for i in a:
    if i in b:
        if i not in common:
            common.append(i)

print(common)
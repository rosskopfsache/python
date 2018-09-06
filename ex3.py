#!/usr/bin/python3

limit = int(input("Whats the limit (number)?: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
i = 0
for item in a:
    if item < limit:
        #print(item)
        b.append(a[i])
    i = i + 1
print(b)
#!/usr/bin/env python

def isPalindrome(s):
    s=str(s)
    if s == s[::-1]:
        return True
    else:
        return False

threes = range(100,1000)
L=[]

for i in threes:
    for j in threes:
        p = i*j
        if isPalindrome(p):
            L.append(p)

L.sort()
print(L[-1])

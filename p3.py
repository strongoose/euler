#!/usr/bin/env python

from math import *

def factorise(originalNumber):
    currentFactor = originalNumber
    possibleFactors = range(2, floor(originalNumber**0.5)+1)
    primeFactors = []
    while True:
        topOfLoopFactor = currentFactor
        for n in possibleFactors:
            if currentFactor % n == 0:
                currentFactor = int(currentFactor/n)
                primeFactors.append(int(n))
                break
        if currentFactor == 1 or currentFactor == originalNumber:
            break
        if currentFactor == topOfLoopFactor:
            primeFactors.append(currentFactor)
            break
    return primeFactors

print(factorise(5*10**12+123))

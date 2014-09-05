#!/usr/bin/env python

from math import *

def sieve(N):
    Ns = [x for x in range(2,N+1)]
    for p in Ns:
        if p != 0:
            for j in range(2,floor(N/p)+1):
                Ns[p*j-2] = 0
    return [ x for x in Ns if x != 0 ]

def factorise(originalNumber):
    currentFactor = originalNumber
    possibleFactors = sieve(floor(originalNumber**0.5)+1)
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

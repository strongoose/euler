# Problem:
#
#     The prime factors of 13195 are 5, 7, 13 and 29.
#
#     What is the largest prime factor of the number 600851475143 ?

from math import *

def prime_factorise(originalNumber):
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

print(max(prime_factorise(600851475143)))

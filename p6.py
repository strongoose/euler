#!/usr/bin/env python

def sumOfSquares(ns):
    S = 0
    for i in ns:
        S = S + i**2
    return S

def squareSum(ns):
    S = 0
    for i in ns:
        S = S + i
    return S**2

def sqsDiff(ns):
    return squareSum(ns) - sumOfSquares(ns)

print(sqsDiff(list(range(1,101))))

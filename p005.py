# Problem:
#
#     2520 is the smallest number that can be divided by each of the
#     numbers from 1 to 10 without any remainder.
#
#     What is the smallest positive number that is evenly divisible by
#     all of the numbers from 1 to 20?
#

import math
import collections

def factorise(n): # return primes up to n
    N = n
    L = range(2, math.ceil(n**0.5)+1)
    P = []
    while True:
        for i in L:
            N = n
            if n % i == 0:
                n = n/i
                P.append(int(i))
                break
        if n == 1:
            break
        if n == N:
           P.append(int(N))
           break
    return P

def multiCUnion(Cs): # takes list of counters and
                     # produces a union of the lot
    if Cs == []:
        return collections.Counter()
    else:
        return multiCUnion(Cs[:-1]) | Cs[-1]

def counterProduct(C):
    P=1
    for i in C:
        P = P * i**C[i]
    return P

def LCM(ns):
    Cs = []
    for i in ns:
        Cs.append(collections.Counter(factorise(i)))
    P = multiCUnion(Cs)
    lcm = counterProduct(P)
    return lcm

print(LCM(list(range(1,21))))

# Problem:
#
#     The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#     Find the sum of all the primes below two million.
#

from math import *

# This one uses the Sieve of Eratosthenes for finding primes
# efficiently.

def sieve(N): # use the Sieve to find all primes up to N
    Ns = [x for x in range(2,N+1)]
    for p in Ns:
        if p != 0:
            for j in range(2,floor(N/p)+1):
                Ns[p*j-2] = 0
    return [ x for x in Ns if x != 0 ] # Suddenly this line is making me think this could be nicely implemented with recursion.

def solve():
    N = 2*(10**6)

    S = 0
    for p in sieve(N):
        S = S + p

    return S

if __name__ == '__main__':
    print(solve())

# Problem:
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
## Note: this is a rather naive first attempt, and takes ages. p10-sieve.py is much, much better.

from itertools import count

def primesBelow(N): # scan numbers for primes below N
    allN = count(2)
    P = []
    for n in allN:
        nIsP = True
        #print('Testing for ' + str(n))
        for p in P:
            if n % p == 0:
            #    print(str(p) + ' divides ' + str(n))
                nIsP = False
                break
        if nIsP:
            P.append(n)
        if n >= N:
            break
    return(P)

N = 2000000

#S = 0
#for p in primesBelow(N):
#    S = S + p

#print(S)

print(primesBelow(N))

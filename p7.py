#Problem:
#
#    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#    What is the 10 001st prime number?
#

from itertools import count

def primeScan(N): # scan numbers indefinitely until we've found the nth prime
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
        if len(P) == N:
            break
    return(P)

print(primeScan(10001)[-1])

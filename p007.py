'''
Problem:

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
    can see that the 6th prime is 13.

    What is the 10 001st prime number?

'''

from itertools import count

def scan_for_primes(big_n):
    '''
    Check each positive integer until we've found the nth prime.
    '''
    all_n = count(2)
    primes = []
    for num in all_n:
        num_is_prime = True
        for prime in primes:
            if num % prime == 0:
                num_is_prime = False
                break
        if num_is_prime:
            primes.append(num)
        if len(primes) == big_n:
            break
    return primes

def solve():
    '''
    Solve the problem.
    '''
    return scan_for_primes(10001)[-1]

if __name__ == '__main__':
    print(solve())

'''
Problem:

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
'''

from math import floor

# This one uses the Sieve of Eratosthenes for finding primes
# efficiently.

def sieve(num): # use the Sieve to find all primes up to N
    '''
    Find primes up to N using the seive of erosthenes.
    '''
    nums = [x for x in range(2, num+1)]
    for candidate in nums:
        if candidate != 0:
            for j in range(2, floor(num/candidate)+1):
                # Suddenly this line is making me think this could be
                # nicely implemented with recursion.
                nums[candidate*j-2] = 0
    return [x for x in nums if x != 0]

def solve():
    '''
    Solve the problem.
    '''
    big_n = 2*(10**6)
    ans = 0

    for prime in sieve(big_n):
        ans = ans + prime
    return ans

if __name__ == '__main__':
    print(solve())

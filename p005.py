'''
Problem 005:

    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by
    all of the numbers from 1 to 20?
'''

import math
import collections

def primes_below(num): # return primes up to n
    '''
    Return primes lower than a number
    '''
    factors = range(2, math.ceil(num**0.5)+1)
    primes = []
    while True:
        for i in factors:
            big_n = num
            if num % i == 0:
                num = num/i
                primes.append(int(i))
                break
        if num == 1:
            break
        if num == big_n:
            primes.append(int(big_n))
            break
    return primes

def multi_counter_union(counters):
    '''
    Takes list of counters and produces a union of the lot.
    '''
    if counters == []:
        return collections.Counter()
    else:
        return multi_counter_union(counters[:-1]) | counters[-1]

def counter_product(counter):
    '''
    Works out the product of all the numbers in a counter
    e.g. counter_product([(2, 2), (3, 1), (5, 3)]) = 2*2*3*5*5*5
    '''
    product = 1
    for i in counter:
        product = product * i**counter[i]
    return product

def lcm(nums):
    '''
    Find the lowest common multiple of the numbers in an iterable.
    '''
    counters = []
    for i in nums:
        counters.append(collections.Counter(primes_below(i)))
    counter = multi_counter_union(counters)
    result = counter_product(counter)
    return result

def solve():
    '''
    Solve the problem.
    '''
    return lcm(list(range(1, 21)))

if __name__ == '__main__':
    print(solve())

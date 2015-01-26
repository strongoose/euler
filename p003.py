'''
Problem:

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
'''

from math import floor

def prime_factorise(original_number):
    '''
    Return prime factors of a number
    '''
    current_factor = original_number
    possible_factors = range(2, floor(original_number**0.5)+1)
    prime_factors = []
    while True:
        top_factor = current_factor
        for num in possible_factors:
            if current_factor % num == 0:
                current_factor = int(current_factor/num)
                prime_factors.append(int(num))
                break
        if current_factor == 1 or current_factor == original_number:
            break
        if current_factor == top_factor:
            # NOTE: lots of appends, again
            prime_factors.append(current_factor)
            break
    return prime_factors

def solve():
    '''
    Solve the problem.
    '''
    return max(prime_factorise(600851475143))

if __name__ == '__main__':
    print(solve())

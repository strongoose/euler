'''
Useful maths functions for use in project euler problems.
'''

from math import floor

def factorise(original_number):
    '''
    Return prime factors of a number
    '''
    if original_number == 1:
        return [1]
    current_number = original_number
    possible_factors = range(2, floor(original_number**0.5)+1)
    prime_factors = []
    while True:
        loop_number = current_number
        for num in possible_factors:
            if current_number % num == 0:
                current_number = int(current_number/num)
                prime_factors.append(int(num))
                break
        if current_number == 1 or current_number == original_number:
            break
        if current_number == loop_number:
            prime_factors.append(current_number)
            break
    if not prime_factors:
        # Then the number is prime
        prime_factors = [original_number]
    return prime_factors

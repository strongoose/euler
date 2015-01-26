'''
Problem:

    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 552 = 3025

    Hence the difference between the sum of the squares of the first
    ten natural numbers and the square of the sum is
    3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(nums):
    '''
    Returns the sum of squares of the numbers in an iterable.
    '''
    ans = 0
    for i in nums:
        ans = ans + i**2
    return ans

def square_sum(nums):
    '''
    Returns the squared sum of the numbers in an iterable.
    '''
    ans = 0
    for i in nums:
        ans = ans + i
    return ans**2

def difference_between_squares(nums):
    '''
    Returns the difference between the squared sum and the sum of
    squares of the numbers in an iterable.
    '''
    return square_sum(nums) - sum_of_squares(nums)

def solve():
    '''
    Solve the problem.
    '''
    return difference_between_squares(list(range(1, 101)))

if __name__ == '__main__':
    print(solve())

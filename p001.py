'''
Problem 001:

    If we list all the natural numbers below 10 that are multiples of
    3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
'''

def solve():
    '''
    Solve the problem.
    '''
    ans = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            ans = ans + i
    return ans

if __name__ == '__main__':
    print(solve())

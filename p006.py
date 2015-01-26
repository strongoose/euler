# Problem:
#
#     The sum of the squares of the first ten natural numbers is,
#     1^2 + 2^2 + ... + 10^2 = 385
#
#     The square of the sum of the first ten natural numbers is,
#     (1 + 2 + ... + 10)^2 = 552 = 3025
#
#     Hence the difference between the sum of the squares of the first
#     ten natural numbers and the square of the sum is
#     3025 − 385 = 2640.
#
#     Find the difference between the sum of the squares of the first
#     one hundred natural numbers and the square of the sum.
#

def sumOfSquares(ns):
    S = 0
    for i in ns:
        S = S + i**2
    return S

def squareSum(ns):
    S = 0
    for i in ns:
        S = S + i
    return S**2

def sqsDiff(ns):
    return squareSum(ns) - sumOfSquares(ns)

def solve():
    return sqsDiff(list(range(1,101)))

if __name__ == '__main__':
    print(solve())

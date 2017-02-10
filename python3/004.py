'''
Problem 004:

    A palindromic number reads the same both ways. The largest
    palindrome made from the product of two 2-digit numbers is
    9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit
    numbers.
'''

def is_palindrome(word):
    '''
    Check whether a string is a palindrome
    '''
    word = str(word)
    # Dear future self: the last number in slice notation denotes step,
    # so [::-1] takes the entire string as a slice and reverses it.
    if word == word[::-1]:
        return True
    else:
        return False

def solve():
    '''
    Solve the problem.
    '''
    return max([i*j for i in range(100, 1000) for j in range(100, 1000) if
                is_palindrome(i*j)])

if __name__ == '__main__':
    print(solve())

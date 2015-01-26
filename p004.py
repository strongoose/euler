# Problem:
#
#     A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#     Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(s):
    s=str(s)
    if s == s[::-1]:
        return True
    else:
        return False

threes = range(100,1000)
L=[]

for i in threes:
    for j in threes:
        p = i*j
        if isPalindrome(p):
            L.append(p)

L.sort()
print(L[-1])

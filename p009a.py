# Problem:
#
#     A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^2 + b^2 = c^2
#
#     For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#     There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#     Find the product abc.
#

from math import *

ns = [ x for x in range(1,999) ] # a+b+c = 1000, so a,b,c < 999 (1+1+998=1000)

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def findTriplets(n):
    T = []
    ns = [ x for x in range(1,n+1) ]
    for c in ns:
        print('c = ', c)
        for a in ns[:ns.index(c)]:
            for b in ns[:ns.index(a)]:
                if a**2 + b**2 == c**2:
                    T.append((a, b, c))
    return T

for i in findTriplets(1000):
    if i[0] + i[1] + i[2] == 1000:
        print(i[0],' + ',i[1],' + ',i[2],' = 1000')
        print(i[0]*i[1]*i[2])
        break

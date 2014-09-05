#!/usr/bin/env python

T=0

def fibTo1M():
    L = [1,2]
    while L[-1] < 4*10**6:
        l = len(L)
        L.append(L[l-2] + L[l-1])
    return(L[0:-1])

fs = fibTo1M()

for i in fs:
    if i % 2 == 0:
        T = T + i

print(T)

"""
python program to find the ith order statistic of a list of unsorted numbers in Ø(n) time
"""

import random

def partition(nlist):
    pivot_idx = random.randrange(len(nlist))
    nlist[0],nlist[pivot_idx] = nlist[pivot_idx],nlist[0]
    i = 1
    for j in range(1,len(nlist)):
        if nlist[j] < nlist[0]:
            nlist[j],nlist[i] = nlist[i],nlist[j]
            i+=1
    nlist[i-1],nlist[0] = nlist[0],nlist[i-1]
    return i-1,nlist

def quick_select(nlist,i):
    if len(nlist) == 0:
        return nlist[0]
    else:
        pivot, nlist = partition(nlist)
        if pivot == i:
            return nlist[i]
        elif pivot >  i:
            return quick_select(nlist[:pivot],i)
        else:
            return quick_select(nlist[pivot+1:],i - pivot - 1)
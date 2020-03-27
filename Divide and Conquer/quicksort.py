"""
Implementation of quicksort using the median of the first, last and middle elements ass the pivot element
"""
count = 0

def findPivotPosition(nlist):
    new_list = list(enumerate(nlist))
    if len(new_list) % 2 == 0:
        final_list = [new_list[0],new_list[len(new_list)//2 - 1], new_list[len(new_list)-1]]
    else:
        final_list = [new_list[0],new_list[len(new_list)//2], new_list[len(new_list)-1]]

    final_list.sort(key=lambda x:x[1])
    return final_list[1][0]

def partition(nlist):
    i = 1
    PivotPosition = findPivotPosition(nlist)
    nlist[0],nlist[PivotPosition] = nlist[PivotPosition],nlist[0]
    pivot = nlist[0]
    for j in range(1,len(nlist)):
        if nlist[j] < pivot:
            nlist[i],nlist[j] = nlist[j],nlist[i]
            i+=1
    nlist[i-1],nlist[0] = nlist[0],nlist[i-1]
    return i-1,nlist


def quicksort(nlist):
    global count
    if len(nlist) <= 1:
        return nlist
    else:
        pivot_index, partitioned_list = partition(nlist)
        count+=len(partitioned_list[:pivot_index])
        left = quicksort(partitioned_list[:pivot_index])
        count+=len(partitioned_list[pivot_index+1:])
        right = quicksort(partitioned_list[pivot_index+1:])
        return left + [partitioned_list[pivot_index]] + right

with open('quicksortInput.txt','r') as file:
    nums = [int(i.strip())for i in file.readlines()]

p = quicksort(nums)
if p == sorted(nums):
    print("sorted")
    print(count)
else:
    print("Not sorted")




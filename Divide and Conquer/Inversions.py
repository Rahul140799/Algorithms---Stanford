"""

Program to count the number of split inversions in a list in O(nlogn) time.
Done Using a modified implementation of MergeSort

"""

def count(nlist):
    if len(nlist) == 1:
        return nlist,0
    else:
        mid = len(nlist) // 2
        left,x = count(nlist[:mid])   # Count number of inversions in left subarray
        right,y = count(nlist[mid:])  # Count number of inversions in right subarray
        res,z = countSplitInversions(left,right)  # Count number of inversions between left and right subarray 
    return res,x+y+z



def countSplitInversions(left,right):
    """
    Count number of inversions between left and right subarray
    """
    result = []
    inverisonCount = 0
    while left and right:
        if left[0]<=right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
            inverisonCount += len(left)

    result += left or right

    return result,inverisonCount


with open('inversionInput.txt','r') as fileObj:
    d = fileObj.readlines()
    for i in range(len(d)):
        d[i] = int(d[i])
    print(count(d)[1])

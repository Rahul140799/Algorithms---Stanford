def count(nlist):
    if len(nlist) == 1:
        return nlist,0
    else:
        mid = len(nlist) // 2
        left,x = count(nlist[:mid])
        right,y = count(nlist[mid:])
        res,z = countSplitInversions(left,right)
    return res,x+y+z

def countSplitInversions(left,right):
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

def mergeSort(nlist):
    if len(nlist) > 1:
        mid = len(nlist) // 2

        left = nlist[:mid]
        right = nlist[mid:]

        mergeSort(left)
        mergeSort(right)
        
        

        merge(nlist,left,right)

def merge(nlist,left,right):

    # Traverse through left and right subarrays
    i = 0
    j = 0

    # Traverse through main list
    k = 0
    
    while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nlist[k] = left[i]
                i+=1
            else:
                nlist[k] = right[j]
                j+=1
            k+=1
        
    while i<len(left):
        nlist[k] = left[i]
        i+=1
        k+=1
        
    while j<len(right):
        nlist[k] = right[j]
        j+=1
        k+=1

        



numsList = [2,1,4,6,3,2,4,5]
mergeSort(numsList)


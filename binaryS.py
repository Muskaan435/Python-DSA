def binarySearch(array,target):
    low = 0
    high = len(array)-1

    while (low <= high):
        mid = (low + high)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid-1
            mid = (low + high)//2
        else:
            low = mid +1
            mid = (low + high)//2
    
    return -1


array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44]
target = 19
print("target's index : ",binarySearch(array,target)+1)
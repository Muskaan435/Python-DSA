def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                swap = array[j]
                array[j] = array [j+1]
                array[j+1] = swap

    return(array)

array = [10,12,21,22,15,16]
print(bubbleSort(array))

# input: 578378923
# output: 3 as 7,8,3 are repeting

num = [5,7,8,3,7,8,9,2,3]
count = 0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] == num [j]:
            count +=1

print(count)
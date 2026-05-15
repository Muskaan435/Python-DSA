# data structres are differnt ways to organize data on your computer, that can be used effectively 
def linearSearch(array,key):
    for i in range(0,len(array)):
        if array[i] == key:
            return i+1
    
    return -1


list = [2,5,4,8,3,7,6,1]
key = 8
print(linearSearch(list,key))

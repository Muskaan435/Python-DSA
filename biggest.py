def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]

    for index in range(1,len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]

    print(biggestNumber)

sampleArray = [10,2,4,11,15,2]
findBiggestNumber(sampleArray)
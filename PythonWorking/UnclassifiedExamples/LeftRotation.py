def rotateLeft(numberOfRotations, originalList):
    temporaryList = []

    for i in range(numberOfRotations):
        temporaryList.append(originalList[i])
    
    for i in range(len(originalList)-numberOfRotations):
        originalList[i] = originalList[i+numberOfRotations]
    
    for i in range(numberOfRotations):
        originalList[len(originalList)-numberOfRotations+i] = temporaryList[i]

    return originalList

list12345 = [1,2,3,4,5]

rotateLeft(3, list12345)

print(list12345)
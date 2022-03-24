def arrayManipulation(n, queries):
    listToBeManipulated = [0]*n
    
    for item in queries: # item structure: [a,b,k]
        listToBeManipulated[item[0]-1] = listToBeManipulated[item[0]-1] + item[2]
        # listToBeManipulated[item[1]] = listToBeManipulated[item[1]] - item[2]
        if item[1] != n:
            listToBeManipulated[item[1]] = listToBeManipulated[item[1]] - item[2]

    print("FasterVersion:")
    print(listToBeManipulated)    
    highestNumber = 0
    currentNumber = 0
    for item in listToBeManipulated:
        currentNumber = currentNumber + item
        if currentNumber > highestNumber:
            highestNumber = currentNumber
    print(highestNumber)
    # return highestNumber

def arrayManipulationBrute(n, queries):
    listToBeManipulated = [0]*n
    for item in queries: # item structure: [a,b,k]
        for i in range(item[0]-1, item[1]):
            listToBeManipulated[i] = listToBeManipulated[i] + item[2]
    print("BruteVersion:")
    print(listToBeManipulated)
    print(max(listToBeManipulated))
    # Reconstruct Final Array from SlopeArray?
    # Then return max of Reconstructed Final Array?
    # return max(listToBeManipulated)



list1 = [1, 5, 3]
list2 = [4, 8, 7]
list3 = [6, 9, 1]
list4 = [6, 10, 7]
list5 = [2, 2, 7]

theList = []
theList.append(list1)
theList.append(list2)
theList.append(list3)
theList.append(list4)
theList.append(list5)

arrayManipulation(10, theList)
arrayManipulationBrute(10, theList)


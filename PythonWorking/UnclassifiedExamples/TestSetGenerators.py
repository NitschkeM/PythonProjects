import math
import GenerateSetsOfNumbers

setOfRandomNumbers = GenerateSetsOfNumbers.GetRandomNumbers(100, 0, 100)

print(setOfRandomNumbers)


def printMinValue(set):
    min = set[0]
    for element in set:
        if min > element:
            min = element
    print('Min: ' + str(min))

def printMaxValue(set):
    max = set[0]
    for element in set:
        if max < element:
            max = element
    print('Max: ' + str(max))

def calcMean(set):
    sum = 0
    n = 0
    for element in set:
        sum = sum + element
        n = n + 1
    return sum/n
    # print(sum/n)

def calcSquareDifferences(set, mean):
    squareDifferences = calcSquareDifferences(set, mean)
    for element in set:
        squareDifferences.append(calcSquareDifference(element, mean))
    return (x-mean)**2

def calcVariance(set):
    mean = calcMean(set)
    squareDifferences = calcSquareDifferences(set, mean)
    sumOfSquareDifferences = 0
    for element in squareDifferences:
        sumOfSquareDifferences = sumOfSquareDifferences + element

    


def calcStandardDeviation(set):
    variance = calcVariance(set)
    return math.sqrt(variance)

printMinValue(setOfRandomNumbers)
printMaxValue(setOfRandomNumbers)
calcMean(setOfRandomNumbers)
# calcVariance(setOfRandomNumbers)
# calcStandardDeviation(setOfRandomNumbers)
import random

def GetRandomNumbers(n, min, max):
    setOfRandomNumbers = []
    for i in range(n):
        setOfRandomNumbers.append(random.randint(min,max))
    return setOfRandomNumbers
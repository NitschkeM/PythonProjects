
### Reversing List by Popping ###
### Timing the Code / Execution Time ###
numberOfElements = 3700000
orderedList = list(range(numberOfElements))
reversedList = list()

import time
start = time.time()
for i in range(numberOfElements):
    reversedList.append(orderedList.pop())
end = time.time()
print(end - start)
##############################################################


# listContainingSequenceOfNumbers =   [5, 2, 4, 6, 1, 3]
listContainingSequenceOfNumbers =   [5,2,4,6,1,3]
for i in range(0, len(listContainingSequenceOfNumbers)):
    print(
        'Index: ' + str(i) + 
        '   ElementNumber: ' + str(i+1) +
        '   Element: ' + str(listContainingSequenceOfNumbers[i]))


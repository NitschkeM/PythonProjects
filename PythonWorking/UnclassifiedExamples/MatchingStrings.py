# def matchingStrings(strings, queries):
#     result = []
#     for i in range(len(queries)):
#         result.append(0)
#         for item in strings:
#             if queries[i] == item:
#                 result[i] = result[i] + 1
#     return result


# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']


# print(matchingStrings(strings, queries))

# Create list of length 10 containing 0's
# myList = [0] * 10
# print(myList)

# Create list of length 10 containing numbers in inclusive interval 0-9:
# myList = list(range(10))
# print(myList)


# max(list) returns a single number even if there are multiple numbers that are maximum.
# myList = [10, 10, 4,3,2,1]
# print(max(myList))

# def loopGivenInterval(interval):
# def printEachNumberInInterval(interval):
#     print(interval)
#     for i in range(interval[0], interval[1]+1):
#         print(i)
        

# intervals = [[1,3], [4,5], [5,9]]
# for interval in intervals:
#     printEachNumberInInterval(interval)


# input = input("Input: ")
# print(input)

# usersOutputIntoComputer = input("Input: ")
# print(usersOutputIntoComputer)

# When you ask a user for input, you are asking them to output something.
# Their output is the input you receive.
# The output they produce is the input you consume.
# The output they give is the input you receive.

for i in range(21):
    print(i*15)
# string = 'string'

# for character in string:
#     print(character)

#####################################################################################################

# This code is not missing or lacking anything.

# string = 'kalle'
# previousCharacter = ''

# for character in string:
#     if character == previousCharacter:
#         print("character == previousCharacter is true")
#     else:
#         print(character)
#     previousCharacter = character


#####################################################################################################

### Comparison of Python and C# Syntax. (C-Like Syntax?)

# string    stringName = "stringValue"  ;
#           stringName = "stringValue"

# int       intName = 0  ;
#           intName = 1

#####################################################################################################
# Continious and Immediate
#   Can there be experience without an experiencer?
#####################################################################################################
# listOfNumbers = list(range(10))
# # print(listOfNumbers)

# prevNum = 0
# for number in listOfNumbers:
#     print(prevNum)
#     print(number)
#     prevNum = number

#####################################################################################################

# listOfIntegers = list(range(10))
# listOfIntegers = [10, 1, 3, 4, 7, 8, 5, 6, 9, 2, 0]
listOfIntegers = list(range(-10,11))

# highestSum = 0
# for integer in listOfIntegers:
#     if (integer < 0):
#     # if (integer > 0):
#         # print(integer)
#         listOfIntegers.remove(integer)
# # print(listOfIntegers)

sum = 0
for i in range(len(listOfIntegers)):
	if (listOfIntegers[i] > 0):
		sum = sum + listOfIntegers[i]
print(sum)
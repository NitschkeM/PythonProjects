# def myFunc(myParam):
#     print(myParam)
#     myFunc(myParam + 1 )
# myFunc(0)


# Functions Performing Operations on Sequences of Numbers



# # DifferenceBetween Terms Function
# def DifferencesBetweenTermsInSequence(sequence):
#     result = []
#     for i in range(len(sequence)):
#         result[i] = sequence[i+1] - sequence[i]
#     return result

# # list(range(a,b)) results in a list with b-a elements: (0,1) -> [0] || (1,10) -> [9 numbers] -> [1,2,3,4,5,6,7,8,9]

# numberSequence = list(range(1,10))
# print(DifferencesBetweenTermsInSequence(numberSequence))





# sequence = [1,2,3,4,5,6,7,8,9,10]

# print(len(sequence))

# for i in range(len(sequence)):
#     print(i)

# for i in range(2,25, 3):
#     print(i)

# class MyClass:
#     def isThisMyClass(self):
#         return True
    # def __bool__ ():
    #     return false
    # # def __len__():
    # #     return 0

# instanceOfMyClass = MyClass()
# print(instanceOfMyClass.isThisMyClass())




# def func():
#     sequence = list(range(1,10))
#     return sequence

# print(func())

users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein", "friends": [{"id": 0, "name": "Hero"}] }
]

# print(users[0])             # list[number] returns element at index number
# print(users[4])
# print(users[0]["name"])     # dictionary["name"] returns a value
# print(users[4]["id"])
#print(users[0][0])         # dictionary[index] does not return a Name:Value Pair
#print(users[4][1])

for user in users:
    user["friends"] = []

# print(users[9])                 # Returns Dictionary representing a user
# print(users[9]["friends"])      # Returns List representing Friends of a user
# print(users[9]["friends"][0])   # Index out of range Error
# print(users[9]["friends"])      # Does not run, becuase previous line was an Error. --> Errors stops/halts execution?

# print(users[9])
# print(users[9]["friends"])
# print("Appending users[0]")
# users[9]["friends"].append(users[0])
# print(users[9]["friends"][0])



# print("users[9]" + users[9])      # TypeError: can only concatenate str (not "dict") to str
print("users[9]" + str(users[9]))
print(str("users[9]" + str(users[9])))
# print(str("users[9]" + users[9])) # TypeError: can only concatenate str (not "dict") to str

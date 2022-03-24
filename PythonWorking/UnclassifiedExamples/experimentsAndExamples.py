# import array

# orderedArray = array.array('b', (1, 2, 3, 4, 5, 6, 7, 8, 9))
# orderedArray = array.array('b', range(1, 10))
# unOrderedArray = array.array('b', (1, 2, 3, 4, 5, 6, 7, 9, 8))


# def isOrdered(array):
#     for i in range(len(array)):
#         print(array[i])
#         if i+1 != array[i]:
#             return False
#     return True

# if isOrdered(orderedArray):
#     print('Is Ordered')
# else:
#     print('Is Not Ordered')

# if isOrdered(unOrderedArray):
#     print('Is Ordered')
# else:
#     print('Is Not Ordered')

# def isOrdered(array):
#     for i in range(len(array)):
#         print(array[i])
#         if i+1 != array[i]:
#             print('Is Not Ordered')
#             return
#     print('Is Ordered')

# isOrdered(orderedArray)
# isOrdered(unOrderedArray)



# originalCollection = list([1, 2, 3, 4])

# def squareCollection(collection):
#     for i in range(len(collection)):
#         collection[i] = collection[i] ** 2
#         print(collection[i])

# squareCollection(originalCollection)
# print(originalCollection)


# notOrderedList = list([1, 2, 5, 3, 6, 4, 7])
# tooChaoticList = list([1, 5, 2, 3, 4, 6, 7])
# tooChaoticList2 = list([2, 5, 1, 3, 4])

# notOrderedList2 = list([1,2,5,3,7,8,6,4])
# 5-3
# 5-4
# 7-5
# 8-6
# 8-7

# # Complete the minimumBribes function below.
# def minimumBribes(q):
#     swaps = 0
#     elementsFoundOutOfOrder = []
#     for i in range(len(q)):
#         if i+1 != q[i]:
#             if elementsFoundOutOfOrder.count(q[i]) > 1:
#                 print('Too Chaotic')
#                 return
#             elementsFoundOutOfOrder.append(q[i])
#             for j in range(i+1, len(q)):
#                 # if i+1 == q[j]:
#                 if q[i] > q[j]:
#                     swap(i, j, q)
#                     swaps = swaps + 1
#     print(swaps)

# def swap(i, j, q):
#     tmp = q[i]
#     q[i] = q[j]
#     q[j] = tmp

# minimumBribes(notOrderedList2)
# print(notOrderedList2)
# # minimumBribes(tooChaoticList2)
# # print(tooChaoticList2)
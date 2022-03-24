# Hyp: The Sum of the First N Odd Numbers is N^2.
# Q: Is the Sum of the First N Odd Numbers N^2?
# A: By Demonstration In Python Code In Visual Studio Code


# Demonstrated: Have now Printed the First 1000 Odd Numbers In Python.
# def printOddNumbers():
#     return list(range(1, 2000, 2))
#     # print(list(range(1, 2000, 2)))
# print(len(printOddNumbers()))


# Q: How to Verify that a Number is a Square Number?

# Q: How to print sums of the first N odd numbers?
# Printing Sum of First 5 Odd Numbers:
# def PrintSumOfFirstFiveOddNumbers():
#     print(1 + 2 + 3 + 4 + 5)
# print(1 + 2 + 3 + 4 + 5)
# A: 15
# Q: Is 5^2 = 15 ?
#   A: No, false, because: 5^2 == 5*5 == 25
# Q: Are the 5 numbers above "The First 5 Odd Numbers"?
# A: No, they are the first 5 "Counting Numbers", Not Counting 0 as a Counting Number.


# RE-Q: How to print sums of the first N odd numbers?
# Simplify-Q: How to print the sum of the first 5 odd counting numbers?
# def PrintSumOfFirstFiveOddCountingNumbers():
#     print(1+3+5+7+9)
# PrintSumOfFirstFiveOddCountingNumbers()
# Result/Output: 5^2 = 25

# RE-Q: How to print sums of the first N odd numbers?
# def PrintSumsOfOddCountingNumbersWithinRange(start,end):
#     range(start, end + 1)

# RE-Q: How to print sums of the first N odd numbers?
# def PrintSumsOfFirstNOddNumbers(n):                                      # Readability?
#     for i in range(2*n):
#         if i % 2 == 0:
#             # i mod 2 is 0, if i am odd.

# Return Number of Odd Numbers between 0 and N:
def ReturnNumberOfOddNumbersBetween0AndN(N):
    counter = 0
    for i in range(N):
        if i % 2 != 0:
            counter = counter + 1
    return counter

print(ReturnNumberOfOddNumbersBetween0AndN(22))         # Eleven Odd Numbers In Interval [0,22]
print(ReturnNumberOfOddNumbersBetween0AndN(33))         # Sixteen Odd Numbers In Interval [0,33]
print(ReturnNumberOfOddNumbersBetween0AndN(44))         # Twenty Two Odd Numbers In Interval [0,44]
print(ReturnNumberOfOddNumbersBetween0AndN(256))        # One Hundred And Twenty Eight Odd Numbers In Interval [0,256]
print(ReturnNumberOfOddNumbersBetween0AndN(512))        # Two Hundred And Fifty Six Odd Numbers In Interval [0,512]
print(ReturnNumberOfOddNumbersBetween0AndN(1024))       # Five Hundred And Twelwe Odd Numbers In Interval [0,1024]



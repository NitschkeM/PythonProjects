# Is it True?
# Does it Make Sense?
# Can I Trust It?

# class TimeClass:
#     def DaysToSeconds(self, numberOfDays):          # The method informs Potential User of What It Expects To Receive / What it can process.
#                                                     # A user might say: "I like it when the function tells me what kind of arguments it expects/can receive/can process".
#                                                     # And: "I like it when I know who/what?# Is This?
#                                                         # Pixels on a Screen

# class TimeClass:
#     def DaysToSeconds(self, numberOfDays):
#         return numberOfDays*24*60*60

# timeClassObject = TimeClass()
# print(timeClassObject.DaysToSeconds(1))
# print(timeClassObject.DaysToSeconds(3))
# print(timeClassObject.DaysToSeconds(7))

class TimeClass:
    def PrintDaysToSeconds(self, numberOfDays):
        print(str(numberOfDays)+" Days is "+str(numberOfDays*24*60*60)+" Seconds")

timeClassObject = TimeClass()
timeClassObject.PrintDaysToSeconds(1)
timeClassObject.PrintDaysToSeconds(3)
timeClassObject.PrintDaysToSeconds(7)



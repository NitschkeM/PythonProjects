# class ClassName:
#   methodDefinitions

# msdie.py
#   Class definition for an n-sided die.

# Q: Variables
#       Declared? Defined? Initialized?
#   I think:
#       Declared:                   myVar;
#       Initialized:                myVar = 5;      # Variable was declared before
#       Declared and Initialized:   myVar = 5;      # Variable was not declared before / did not exist before

from random import randrange, randint

class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randint(1, self.sides)
        # self.value = randrange(1, self.sides+1)
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value


# Call to class constructor creates/generates an object
# We pass an argument to the constructor
die1 = MSDie(6)
die2 = MSDie(10)
die3 = MSDie(14)
die1Outputs = []
die2Outputs = []
die3Outputs = []

for i in range(1, 12):
    die1.roll()
    die1Outputs.append(die1.getValue())


for i in range(1, 12):
    die2.roll()
    die2Outputs.append(die2.getValue())


for i in range(1, 12):
    die3.roll()
    die3Outputs.append(die3.getValue())


print(die1Outputs)
print(die2Outputs)
print(die3Outputs)
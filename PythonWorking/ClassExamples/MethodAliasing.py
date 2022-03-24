newClass = ''       # Program runs without this variable declaration and initialization.
                    # But there appears yellow lines underneath the usage of the variable named newClass
                    # They appear because without this line, there is no variable named newClass declared in the global scope
                    #   Before is is declared in global scope within the function below.
                    #   Before is is declared for global scope in the local scope of the function below.
def DefineClassWithAliasedMethod_And_InitializeGlobalVariableHoldingInstanceOfClass():
    class ClassWithAliasedMethod():
        def add(self,a,b):
            return a+b
        adder = pluss = add
    # nonlocal newClass
    global newClass
    newClass = ClassWithAliasedMethod()

def ClassWithAliasedMethodIsNeeded():
    return True

if ClassWithAliasedMethodIsNeeded():
    DefineClassWithAliasedMethod_And_InitializeGlobalVariableHoldingInstanceOfClass()

# newClass = ClassWithAliasedMethod()

print(newClass.add(33,33))
print(newClass.pluss(22,22))
print(newClass.adder(11,11))


# Syntax as how something CAN be written?
# Syntex as rules for how something can be written? --> SyntaxRules

# Syntax, Rules, Constructs?
# To use this Programming Construct, use the following Syntax?
# To use the if programming construct, use the following syntax?:
#   if Condition:
#       Statements
# if TrueFalseCondition:
#       Statements
# if TrueFalseQuestion(s):
#       Statements
# if ThereIsTime() && ThereIsSpace():
#   Statements
# if EnoughTime() && EnoughSpace():
#   Statements

#   True && True == True
#   True && False == False
#   False && True == False
#   FFalse && False == False

#   True and True is True
#   True and False is False
#   False and True is False
#   False and False is False

# if I am Hungry and There is Lasagne:
#   I can eat Lasagne

# if IsHungry and IsLasagne:
#   LasagneCanBeEatenNow
# else:
#   LasagneCanNotBeEatenNow

# if IsHungry and IsLasagne:
#   I want to eat lasagne now
# else:
#   I dont want to eat lasagne now

# IsHungry and IsLasagne        --> I want to eat lasagne now           --> Eat lasagne now is Todo
# IsHungry and IsNotLasagne     --> I dont want to eat lasagne now      --> Eat lasagne now is Not Todo
# IsNotHungry and IsLasagne     --> I don't want to eat lasagne now     --> Eat lasagne now is Not Todo
# IsNotHungry and IsNotLasagne  --> I do not want to eat lasagne now    --> Eat lasagne now is Not Todo


# Helpful   - NotHelpful    - UnHelpful
# Useful    - NotUseful     - UnUseful                   - UnUsable? else: NotUseful but can be used
# True      - NotTrue       - UnTruthful/UnTrue - False

# Is something that is (NotHelpful and NotUseful and NotTrue)   Usable?     Is it Wise to Use? Is it Wise to do?
# Is something that is (Helpful and Useful and NotTrue)         Usable?     Is it Wise to Use? Is it Wise to do?
# Is something that is (Helpful and NotUseful and NotTrue)      Usable?     Is it Wise to Use? Is it Wise to do?
# Is something that is (NotHelpful and Useful and NotTrue)      Usable?     Is it Wise to Use? Is it Wise to do?

# Do we even have examples of these?
# Not that we have been made aware of?

# For what Purpose?
# In what Context?

# Life, Decision Making, What to do
#   Life as Whole and Daily Life

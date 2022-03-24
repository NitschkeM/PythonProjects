# my_file = open("FileOutputDirectory/pythonDataFlowSample1_Output.txt", "w") # Creates file if file does not exist.
filePath = 'D:\Software-Development\Projects\PythonProjects\PythonWorking\FileOutputDirectory\pythonDataFlowSample1_Output.txt'

# ClassVariables? - Variables Inside Classes / Variables Belonging to Classes?
# Data Attributes   - Python
# Instance Variables- Smalltalk
# Data Members      - C++
# Member Variables? - C#?

# Function Definitions  - The way to define functions in Python --> def statements
# Class Definitions     - The way to define classes in python   --> class statements
# Method Definitions    - The way to define methods in python   --> def statements withon class statements == function definitions within class definitions?
# function definitions within class definitions?
#       We use function definitions inside a class to define the methods of that class.

# Creation Definition, Declaration
# Assignment, Initialization
# Declare functions? Declare classes? Declare methods?
# Define functions and classes
# Declare variables?
# Assign Values to Variables --> Variables contains something - the variables content - the variables value.
# Initialization of a variables value? Initialize its value?
# Initialize a variable?
    # Initialize a variables value? Initialize the value of a variable?
    # To assign/give/set the variables first value, 
    # The variable might change later
        # The value might change later

#################### VARIABLES ####################
# Variable: A named location in memory consisting of bits/bytes.
#       The configuration of the bits an bytes represents the value of that variable.
#       Change the bits and bytes at the location the VariablePointsTo/VariableRepresents --> To change the value of the variable.

# Variable as Pointing to a Location in Memory, as pointing to a MemoryLocation
# Variable as Representing a Location in Memory, as representing a MemoryLocation

# Variable as a MemoryAddress? As the address of a MemoryLocation?
# Human Readable representation of a particular/reserved MemoryLocation: The Variable Name?
# Machine/LowerLevel representation of a particular MemoryLocation: The Memory Address?

# Variables Names points to a Particular and Reserved MemoryLocation?
# MemoryAddresses points to a Particular, but not necessarily Reserved MemoryLocation?
# MemoryAddresses points to a Particular MemoryLocation?

# Computer/Hardware memory as consisting of bits/bytes.

# Parameter
# Parameter Variable?
# Parameter Variable Name?
# Argument
# Argument Variable?
# Argument Variable Name?


class FileReaderWriter:
    def CreateFileWriteThreeLines(self, filePath):
        my_file = open(filePath, "w")  # Creates file if file does not exist.
        my_file.write("First Line\n")
        my_file.write("Second Line\n")
        my_file.write("Third Line")

    def ReadFilePrintContent(self, filePath):
        my_file = open(filePath)         # "r"/read is the default mode
        content = my_file.read()
        print(content)
        my_file.close()

FileReaderWriter.CreateFileWriteThreeLines(filePath)
FileReaderWriter.ReadFilePrintContent(filePath)

# CreateFileWriteThreeLines(filePath)
# ReadFilePrintContent(filePath)



# D:\Software-Development\Projects\PythonProjects\PythonWorking\FileOutputDirectory\pythonDataFlowSample1_Output.txt

# Calling a function executes its lines of code
# Calling a function executes its statements
# Function consisting of statements

# Class consisting of statements? - Declaring/Defining/Initialization Statements? Creation Statements?
# Class consisting of Methods/Functions and Variables

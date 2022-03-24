# from .PrintElementsOfLinkedList import printLinkedList
def printLinkedList(head):
    # If I change head inside this function, do I then change head outside this function?
    # If I change the parameter inside a function, do I then change the argument outside the function?
    #       Has to do with Pointers? Memory Locations? What the VariableNames represent?
    #       Do the argument and parameter Point to the Same MemoryLocation/Object?
    currentNode = head                  
    while currentNode:
        print(currentNode.data)
        currentNode = currentNode.next

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def insertNodeAtTail(head, data):
    # Here it is assumed that I can change the Argument Outside the function, by changing the Parameter Inside the function
    #   It is not changed - yet no longer assumed.
    #   Instead we changed how the function was used --> A call to the function ReSets/ReAssigns singlyLinkedList.head
    if not head:
        head = SinglyLinkedListNode(data)
    else:
        currentNode = head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = SinglyLinkedListNode(data)
    return head


# There is a conradiction in our implementation.
# Scenario 1: head is None:
#   Implementation assumes changing value of currentNode also changes value of head
# Scenario 2: head is not None:
#   Implementation assumes changing value of currentNode does not change value of head

singlyLinkedList = SinglyLinkedList()

singlyLinkedList.head = insertNodeAtTail(singlyLinkedList.head, 5)
singlyLinkedList.head = insertNodeAtTail(singlyLinkedList.head, 6)
singlyLinkedList.head = insertNodeAtTail(singlyLinkedList.head, 7)

# print(singlyLinkedList.head)
# print(singlyLinkedList.head.data)
printLinkedList(singlyLinkedList.head)

print("Done")

####################### Questions, Argument, Param, Integer(SimpleVar), Object ###########################
# Integer is passed: a copy is used in function => change in param !=> change in arg
# Object is passed: a prop of object is changed --> Change is visible both inside and outside function --> Change in param => Change in Arg
#       The VariableName used as an argument - passed to the function
# AND   The VariableName used as a parameter - received by the function
#       Points to the same Underlying Object / Memory Address / Location in Memory

#   The VariableName is a MemoryAddress NOT an object?
#   At the MemoryAddress there is an object?
#   At the MemoryAddress there is data that together can be seen as an object?

# But what about when:
#   Property of an Object is passed --> The prop is changed
#       Does this change the property of the object referred to by the VariableName outside the function?
#   A: The property of the ObjectOutside
#           Does NOT change if only the property of the object is passed then changed inside the function.

####################### doesArgumentChangeWhenIChangeParam ###########################
# def doesArgumentChangeWhenIChangeParam(param):
#     param = 5

# argument = 10

# doesArgumentChangeWhenIChangeParam(argument)
# print(argument)

####################### doesObjectArgumentChangeWhenIChangeParamProperty ###########################

# class MyObject:
#     def __init__(self, param):
#         super().__init__()
#         self.myProp = param

# def doesObjectArgumentChangeWhenIChangeParamProperty(objParam):
#     objParam.myProp = 5

# myObject = MyObject(10)

# print(myObject.myProp)
# doesObjectArgumentChangeWhenIChangeParamProperty(myObject)
# print(myObject.myProp)


####################### doesOutsideObjectChangeIfOnlyPropertyIsPassedAndChanged? ###########################

# class MyObject:
#     def __init__(self, param):
#         super().__init__()
#         self.myProp = param

# def doesOutsideObjectChangeIfOnlyPropertyIsPassedAndChanged(ObjPropParam):
#     ObjPropParam = 5

# myObject = MyObject(10)

# print(myObject.myProp)
# doesOutsideObjectChangeIfOnlyPropertyIsPassedAndChanged(myObject.myProp)
# print(myObject.myProp)


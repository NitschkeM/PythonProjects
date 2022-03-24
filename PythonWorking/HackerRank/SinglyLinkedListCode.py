class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def printLinkedList(head):
    # If I change head inside this function, do I then change head outside this function?
    # If I change the parameter inside a function, do I then change the argument outside the function?
    #       Has to do with Pointers? Memory Locations? What the VariableNames represent?
    #       Do the argument and parameter Point to the Same MemoryLocation/Object?
    currentNode = head                  
    while currentNode:
        print(currentNode.data)
        currentNode = currentNode.next

def insertNodeAtTail(head, data):
    # Here it is assumed that I can change the Argument Outside the function, by changing the Parameter Inside the function
    #   It is not changed - yet no longer assumed.
    #   Instead we changed how the function was used --> A call to the function ReSets/ReAssigns singlyLinkedList.head (head is returned)
    if not head:
        head = SinglyLinkedListNode(data)
    else:
        currentNode = head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = SinglyLinkedListNode(data)
    return head

def reversePrint(llist):
    currentElement = llist
    tmpList = list()
    # When currentElement.next == None, currentElement is the last element
    while currentElement.next != None:          # For each Iteration:
        tmpList.append(currentElement.data)         # Do the thing      / Perform Operation
        currentElement = currentElement.next        # Go to next        / Increment             / change that which loop condition depends on
    tmpList.append(currentElement.data)         # Do the thing      / Perform Operation
    
    # counter = len(tmpList) - 1
    # while counter >= 0:
    #     print(tmpList[counter])
    #     counter = counter - 1
    tmpList.reverse()
    for element in tmpList:
        print(element)

def reverse(head):
# def reverse(sll):
#     head = sll.head

    if head == None:   # Empty List, head==None, returns head
        return None
        # return sll

    currentNode = head.next
    head.next = None
    # sll.tail = head
    previousNode = head
    
    # while not isLastNode(currentNode):
    # while currentNode.next != None:
    while currentNode != None:
        # Before changing currentNode.next:     Store currentNode.next somewhere else
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    
    # sll.head = previousNode
    # return sll
    return previousNode

linkedList1 = SinglyLinkedList()
linkedList2 = SinglyLinkedList()
linkedList3 = SinglyLinkedList()

for i in range(3):
    linkedList1.head = insertNodeAtTail(linkedList1.head, i)
for i in range(3,6):
    linkedList2.head = insertNodeAtTail(linkedList2.head, i)
for i in range(6,10):
    linkedList3.head = insertNodeAtTail(linkedList3.head, i)

printLinkedList(linkedList1.head)
linkedList1.head = reverse(linkedList1.head)
printLinkedList(linkedList1.head)
# reversePrint(linkedList1.head)


# printLinkedList(linkedList.head)
# reversePrint(linkedList1.head)
# reversePrint(linkedList2.head)
# reversePrint(linkedList3.head)

# noneVar = None
# print(noneVar.nonExistingProperty)

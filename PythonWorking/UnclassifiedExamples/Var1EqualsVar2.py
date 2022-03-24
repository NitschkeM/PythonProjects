# class MyClass:
#     def __init__(self):

class SinglyLinkedList:
    def __init__(self):
        self.head = None

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


# singlyLinkedList = SinglyLinkedList()

# var2 = singlyLinkedList
# singlyLinkedList.head = SinglyLinkedListNode(5)
# singlyLinkedList.head.data = 15

# print(singlyLinkedList == var2)
# print(singlyLinkedList.head == var2.head)


# var3 = 6
# var4 = var3
# var3 = 15

# print(var3 == var4)

sll = SinglyLinkedList()
sll.head = SinglyLinkedListNode(5)
sll.head.next = SinglyLinkedListNode(10)

node1 = sll.head
node2 = sll.head.next

var3 = node2
node2 = None

# print(sll.head.next.data)
print(node1.data)
print(node2)
print(var3.data)



#   singlyLinkedList.head.data
# How do I understand this line of code? Multiple ways/perspectives?
#   Accessing Instance Variable of object: head
#   Accessing Property of object through pointer to object: head
#   Using a pointer to an object to access its instance variable


# Using a pointer to an object to access its instance variable (singlyLinkedList.head)
# which is a pointer to an object through which we access the instance variable of the second object (.head.data)
# which is a pointer to a value? (.data)
# which can be seen as both a value and a pointer to a value (.data)
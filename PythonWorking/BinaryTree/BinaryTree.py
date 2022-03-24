# TODO: Implement BinaryTree.add(node)
#   Q: Does Adding behavior depend on Traversal Behavior?
#   A: We traversed when we added in the Linked List Structure.
#   A: But could it not be possible to keep track of where we want to add the next Node?
#       Then Adding would be O(1) - independent on how many elements were in the Tree.
#       The add function would have to update this tracker/variable.
# What about a Binary Counter for keeping track of/knowing where to add next node?
#   That would depend on the tree being balanced.
# TODO: Traversal
#   We have the idea that a Stack and Recursion could be useful for tree traversal.


# Suggestion for NEXT TASK:
#   Create Adding Function and keep track of where to add next node.
#   Add such that the tree is balanced and assume the tree is always balanced.
#       Then we can attempt to create more functionality that Keeps the Tree balanced.
#       Or perhaps a Balancing Function?
#           Where add function just depends on a pointer/variable that keeps track of an available space.

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    # What happens if self.head does not exist?
    # - It never exists, it is always created here in the __init__ method, the constructor method of the class.
    #   - Could the __init__ method be accessed through an instantiated object?
    #       - Would that make sense?
    def __init__(self, head):
        self.head = head

    # def add(self, value):
    #     if self.head.left == None:
    #         self.head.left = BinaryTreeNode(value)
    #     else:
    #         self.head.right = BinaryTreeNode(value)
    # def add(self, value):
    #     if self.head == None:
    #         self.head = BinaryTreeNode(value)
    #     if self.head.left == None:
    #         self.head.left = BinaryTreeNode(value)
    
    def isEmpty(self):
        return self.head == None
    

def hasLeftChildNode(node):
    if node.left == None:
        return False
    else:
        return True

def printParentNodeAndLeftRightChildren(topNode):
    print(topNode.value)
    print(topNode.left.value)
    print(topNode.right.value)

binaryTree = BinaryTree(BinaryTreeNode(1))

for i in range(2,4):
    binaryTree.add(i)

# if not binaryTree.isEmpty():
#     currentNode = binaryTree.head
#     while currentNode.left != None:
#         currentNode = currentNode.left

printParentNodeAndLeftRightChildren(binaryTree.head)
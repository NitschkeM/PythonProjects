class BinaryTreeNode:
    # def __init__(self, value, parent):
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

headNode = BinaryTreeNode(1)
headNode.left = BinaryTreeNode(2, headNode)
headNode.right = BinaryTreeNode(3, headNode)

def printParents(topNode):
    print(topNode.parent)
    print(headNode.left.parent, headNode.left.value)
    print(topNode.right.parent)

printParents(headNode)



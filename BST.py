class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.key)
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.key)

def printPreorder(root):
    if root:
        print(root.key)
        printPreorder(root.left)
        printPreorder(root.right)

root=Node(5)
node1=Node(6)
root.left=node1
node2=Node(14)
root.right=node2
node3=Node(4)
root.left.left=node3
node4=Node(5)
root.left.right=node4

printInorder(root)
print()
printPostorder(root)
print()
printPreorder(root)
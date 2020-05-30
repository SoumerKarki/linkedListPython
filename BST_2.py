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

def searchTree(root,data):
    if root.key==data:
        print(root.key," Found")
        return
    if root is None:
        print("Data not found in the tree!")
        return
    if root.key<data:
        return(searchTree(root.right,data))
    return searchTree(root.left,data)

def insertTree(root,node):
    if root is None:
        root=node
    if root.key<node.key:
        if root.right is not None:
            return insertTree(root.right,node)
        else:
            root.right=node
            return
    else:
        if root.left is not None:
            return insertTree(root.left,node)
        else:
            root.left=node
            return



r=Node(50)

insertTree(r,Node(30))
insertTree(r,Node(20))
insertTree(r,Node(40))
insertTree(r,Node(70))
insertTree(r,Node(60))
insertTree(r,Node(80))

printInorder(r)


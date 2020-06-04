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

def minValNode(root):
    current=root
    while current is not None:
        current=current.left
    return current

def delInTree(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=delInTree(root.left,key)
    elif key>root.key:
        root.right=delInTree(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root.right=None
            return temp
        elif root.right is None:
            temp=root.left
            root.left=None
            return temp
        temp=minValNode(root.right)
        root.key=temp.key
        root.right=delInTree(root.right,temp.key)
    return root




r=Node(50)

insertTree(r,Node(30))
insertTree(r,Node(20))
insertTree(r,Node(40))
insertTree(r,Node(70))
insertTree(r,Node(60))
insertTree(r,Node(80))

printInorder(r)

print()

print("Delete 20")

r=delInTree(r,20)

print()

printInorder(r)

print()

print("Delete 30")

r=delInTree(r,30)

print()

printInorder(r)

class Node:
    def __init__(self):
        self.data=None
        self.next=None

    def setData(self,data):
        self.data=data

    def getData(self):
        return self.data

    def setNext(self,node):
        self.next=node

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next is not None


class Stack:
    def __init__(self,data):
        self.head=None
        if data:
            for i in data:
                self.push(i)

    def push(self,data):
        temp=Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head=temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp=self.head.getData()
        self.head=self.head.getNext()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()


l=['first','second','third','fourth','fifth']
stack=Stack(l)
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())




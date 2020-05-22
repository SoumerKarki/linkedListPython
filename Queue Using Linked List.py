class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def setData(self,data):
        self.data=data

    def setNext(self,next):
        self.next=next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next is not None

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.size=0

    def enqueue(self,data):
        newnode=Node(data)
        if self.front is None:
            self.front = self.rear = newnode
            self.size = self.size + 1
        else:
            self.rear.setNext(newnode)
            self.rear = newnode
            self.size = self.size + 1

    def dequeue(self):
        if self.front is None:
            print("Queue is empty!")
            return
        else:
            delnode=self.front
            self.front=delnode.getNext()
            self.size = self.size - 1
            if self.front is None:
                self.rear = None
            return delnode.getData()

    def printQueue(self):
        tempnode=self.front
        l=[]
        while tempnode is not None:
            l.append(tempnode.data)
            tempnode=tempnode.getNext()
        print(l)


def main():
    q=Queue()
    q.enqueue(1)
    q.enqueue(13)
    q.enqueue(14)
    q.enqueue(11)
    q.enqueue(8)
    q.printQueue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.printQueue()

main()











class L_queue:
    def __init__(self):
        self.clear()
    def enqueue(self,item):
        self.q_list.append(item)
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Unable to dequeue: queue list is empty.")
        return self.q_list.pop(0)
    def isEmpty(self):
        return len(self.q_list) == 0
    def size(self):
        return len(self.q_list)
    def clear(self):
        self.q_list=[]

class C_queue:
    def __init__(self,size):
        self.size = size
        self.clear()
    def enqueue(self,item):
        if self.isFull():
            raise IndexError("Unable to enqueue : queue list is full.")
        if item == None :
            raise TypeError("Unable to enqueue : Inserting None is prohibited")
        self.rear = (self.rear + 1)%self.size
        self.q_list[self.rear] = item
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Unable to dequeue : queue list is empty.")
        self.front = (self.front + 1)%self.size
        item = self.q_list[self.front]
        self.q_list[self.front] = None
        return item
    def isFull(self):
        return self.rear == self.front and self.q_list[self.front] != None
    def isEmpty(self):
        return self.rear == self.front and self.q_list[self.front] == None
    def length(self):
        return (self.rear - self.front + self.size)%self.size
    def clear(self):
        self.q_list= [None]*self.size
        self.front = 0
        self.rear = 0
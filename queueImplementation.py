from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.insertleft(val)
    
    def dequeue(self):
        if len(self.buffer) == 0:
            print( "Queue is Empty")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    
if __name__ == '__main__':
    pass

'''Stack can be defined using list (Dynamic Array) or the LinkList 
    the biggest challange in list is its size and in linkList the operation will O(n)
    so Python provides collections.deque class for Stack 
    Lets use that and implement Stack Functionalities'''

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)
    
if __name__=='__main__':
    s = Stack()
    s.push(6)
    s.push(12)
    s.push(0)
    s.push(13)
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.is_empty())
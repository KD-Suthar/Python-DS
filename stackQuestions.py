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
    
def reverse_string(s):
    stack = Stack()
    for word in s:
        stack.push(word)
    str = ''
    while stack.is_empty() == False:
        str += stack.pop()
    return str

def is_matched(word1,word2):
    match_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    return match_dict[word1] == word2

def is_balanced(s):
    stack = Stack()
    for word in s:
        if word == '(' or word == '{' or word == '[':
            stack.push(word)
        elif word == ')' or word == '}' or word == ']':
            if stack.size() == 0:
                return False
            if not is_matched(word,stack.pop()):
                return False
        
    return stack.size() == 0
        
    
if __name__=='__main__':
       
    str = reverse_string("We will conquere COVID-19")
    print(str)
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
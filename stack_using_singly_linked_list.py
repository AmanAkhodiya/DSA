class Node:
    def __init__(self,item,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self,start=None):
        self.start = start
        self.count = 0
        
    def is_empty(self):
        if self.start is None:
            return True
        
    def push(self,item):
        n = Node(item = item,next=self.start)
        self.start = n
        self.count+=1
    
    def pop(self):
        if not self.is_empty():
            self.start = self.start.next
            self.count-=1
        else:
            return 'List is Empty..'
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            return 'List is Empty'
    
    def size(self):
        if not self.is_empty():
            return self.count
        
stk = Stack()
stk.push(5) 
stk.push(10)
stk.push(15)
print(stk.size())
print(stk.peek())
stk.pop()
print(stk.size())
print(stk.peek())

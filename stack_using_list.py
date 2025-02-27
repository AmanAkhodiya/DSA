class Stack:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items) == 0
    
    def insert(self,item):
        try:
            self.items.append(item)
        
        except Exception as e:
            print(f'error when insert item:{e}')
        
    def pop(self):
        try:
            self.items.pop()
            
        except IndexError:
            print('List is empty...')
    
    def peek(self):
        try:
            return self.items[-1]     
        except IndexError:
            print('List is empty...')
    
    def size(self):
        return len(self.items)
    
    
stack=Stack()
stack.insert(1)
stack.pop()
stack.peek()
print(stack.size())
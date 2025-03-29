class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def insert(self,item):
        try:
            self.append(item)
        
        except Exception as e:
            print(f'error when insert item:{e}')
            
    def pop(self):
        try:
            if not self.is_empty():
                super().pop()
            else:
                print('List is Empty.')
        
        except Exception as e:
            print(f'error when pop item:{e}')
            
    def peek(self):
        try:
            if not self.is_empty():
                return self[-1]   
            else:
                print('List is Empty..')  
        except IndexError:
            print('List is empty...')
            
    def size(self):
        return len(self)
    
stack=Stack()
stack.is_empty()
stack.insert(1)
stack.insert(2)
print(stack.peek())
print(stack.size())
stack.pop()
print(stack.peek())

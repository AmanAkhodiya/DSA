class Queue:
    def __init__(self):
        self.list=[]
        
    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        if not self.is_empty():
            self.list.pop(0)
        else:
            return 'List is empty...'
        
    def is_empty(self):
        if len(self.list) ==0:
            return True
        else:
            return False
    
    def size(self):
        if not self.is_empty():
            return len(self.list)
        else:
            return 'List is empty...'
    
    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            return 'List is empty...'
        
    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            return 'List is empty...'
        

q=Queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
print(q.size())
q.pop()
print(q.get_front())
print(q.get_rear())
        
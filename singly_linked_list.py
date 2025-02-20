class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self):
        self.head = None
        
    def inser_node_start(self,item=None):
        node=Node(item=item,next=self.head)
        self.head=node
        return node
    
    def inser_node_end(self,item=None):
        node=Node(item=item)
        temp=self.head
        if temp == None:
            temp=node
            return node
        else:
            while temp:
                if temp.next is None:
                    temp.next = node
                    return node
                else:
                    temp=temp.next
    def search(self,item):
        temp=self.head
        while temp:
            if temp.item==item:
                return temp
            else:
                if temp.next is not None:
                    temp=temp.next
                else:
                    print("None")
                    return None
                
    def inser_node_position(self,add_after,item):
        node = Node(item=item)
        add_after_node=self.search(add_after)
        if add_after_node:
            node.next=add_after_node.next
            add_after_node.next=node
        else:
            return None
            
            
        
    def is_empty(self):
        return self.head
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(f'->{temp.item}',end='') if temp.next else print()
            temp=temp.next
        else:
            return None
    def delete_start(self):
        if self.is_empty():
            self.head=self.head.next
        else:
            print("List is Empty")
    def delete_end(self):
        temp=self.head
        while temp:
            if temp.next.next is None:
                temp.next=None
                return True
            else:
                temp=temp.next
    
    def delete_after(self,item):
        temp=self.head
        if temp.next is None:
            temp = None
        elif temp.next.next is None:
            temp = temp.next.next
        else:
            while temp:
                if temp.item==item and temp.next:
                    temp.next=temp.next.next if temp.next.next else None
                    return True
                elif temp.next:
                    temp=temp.next
                else:
                    print("This is last element.0 element is remain after that.")
                    return None
                
    def delete_this(self,item):
        temp=self.head
        if temp and temp.next == None and temp.item==item:
            temp == None
        else:
            while temp:
                if temp.next.item == item:
                    temp.next = temp.next.next
                    return True
                else:
                    temp = temp.next if temp.next else None
                
                    
    
    
sll=SLL()
sll.inser_node_start(item=240)
sll.inser_node_end(item=340)
sll.inser_node_end(item=540)
sll.traverse()
sll.inser_node_position(add_after=240,item=250)
sll.inser_node_position(add_after=340,item=550)
sll.traverse()
sll.delete_start()
sll.traverse()
sll.delete_end()
sll.traverse()
sll.inser_node_position(add_after=340,item=750)
sll.traverse()
sll.delete_after(250)
sll.traverse()
sll.delete_this(750)
sll.traverse()
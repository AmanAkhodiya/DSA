class Node:
    def __init__(self,item,prev=None,next=None):
        self.item=item
        self.next=next
        self.prev=prev

class CDLL:
    def __init__(self,head=None):
        self.head=head
    
    def insert_at_first(self,item):
        node=Node(item=item)
        if self.head is None:
            node.next=node
            node.prev=node
            self.head=node
        else:
            node.prev=self.head.prev
            node.next=self.head
            self.head.prev.next=node
            self.head.prev=node
            self.head=node
        return node
    def inser_at_last(self,item):
        node=Node(item=item)
        if self.head is None:
            node.prev=node
            node.next=node
            self.head=node
        else:
            node.prev=self.head.prev
            self.head.prev.next=node
            node.next=self.head
            self.head.prev=node
            
    def search(self,item):
        temp=self.head
        if temp is None:
            return "List is empty.."
        else:
            while True:
                if temp.item == item:
                    return temp
                temp = temp.next
                if temp == self.head:
                    return None
            
    def insert_after(self,iaf_item,item):
        if self.head is None:
            return "List is empty.."
        else:
            iaf_node=self.search(item=iaf_item)
            node=Node(item=item)
            if iaf_node:
                if iaf_node.prev==iaf_node and iaf_node.next==iaf_node:
                    node.prev=iaf_node
                    node.next=iaf_node
                    iaf_node.next=node
                    iaf_node.prev=node
                else:
                    node.next=iaf_node.next
                    iaf_node.next.prev=node
                    node.prev=iaf_node
                    iaf_node.next=node
                    
    def delete_first(self):
        if self.head is None:
            return "List is empty.."
        elif self.head.next==self.head and self.head.prev==self.head:
            self.head=None
            return True
        else:
            self.head.prev.next=self.head.next
            self.head.next.prev=self.head.prev
            self.head=self.head.next       
            
    
    def delete_last(self):
        if self.head is None:
            return "List is empty.."
        elif self.head.next==self.head and self.head.prev==self.head:
            self.head=None
            return True
        else:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head

            
    def delete_this(self,item):
        temp=self.search(item=item)
        if self.head is None:
            return "List is empty.."
        if temp:
            if temp.item==self.head.item and temp.next==self.head:
                self.head=None
            elif temp == self.head:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
            else:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev

    def traverse(self):
        temp=self.head
        if temp is None:
            return "List is empty...."
        else:
            while True:
                print(temp.item,end=' ')
                temp=temp.next
                if temp==self.head:
                    print()
                    break
cdll=CDLL()
cdll.insert_at_first(item=30)
cdll.insert_at_first(item=20)
cdll.insert_at_first(item=10)
cdll.inser_at_last(item=40)
cdll.inser_at_last(item=50)
cdll.insert_after(iaf_item=30,item=35)
cdll.traverse()
cdll.delete_first()
cdll.delete_last()
cdll.delete_this(20)
print("-----------")
cdll.traverse()
    
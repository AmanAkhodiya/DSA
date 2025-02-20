class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self):
        self.last=None
        
    def search(self,item):
        temp=self.last
        while temp:
            if temp.item==item:
                return temp
            temp=temp.next
            if temp==self.last:
                print("Item not found in list")
                return None
    def insert_at_start(self,item):
        node=Node(item=item)
        if self.last==None:
            node.next=node
            self.last=node
        else:
            node.next=self.last.next
            self.last.next=node
    def insert_at_end(self,item):
        node=Node(item=item,next=self.last.next)
        if self.last==None:
            node.next=node
            self.last=node
        else:
            node.next=self.last.next
            self.last.next=node
            self.last=node
    def insert_after(self,item,iaf_item):
        if self.last==None:
            return "Any node is not present in list.."
        if self.last.item==iaf_item:
            node=Node(item=item,next=self.last.next)
            self.last.next=node
            self.last=node
        else:
            iaf_node=self.search(item=iaf_item)
            if iaf_node!=self.last:
                node=Node(item=item,next=iaf_node.next)
                iaf_node.next=node
    def traverse(self):
        temp=self.last
        while temp:
            print(temp.next.item,end=" ")
            temp=temp.next
            if temp==self.last:
                print()
                break
    def delete_at_start(self):
        if self.last:
            if self.last ==self.last.next:
                self.last=None
            else:
                self.last.next=self.last.next.next
        else:
            print("Any node is not present in list..")
        
    def delete_at_end(self):
        temp=self.last
        while temp:
            if temp.next==temp:
                self.last=None
                return True
            elif temp.next==self.last:
                temp.next=temp.next.next
                self.last=temp
                return True
            else:
                temp=temp.next
    
    def delete_this(self,item):
        if self.last == None:
            return "Any item not present in list.."
        elif self.last == self.last.next and self.last.item==item:
            self.last==None
        else:
            temp= self.last
            while temp:
                if temp.next.item==item and temp.next!=self.last:
                    temp.next = temp.next.next
                    return True
                elif temp.next.item==item and temp.next==self.last:
                    temp.next=temp.next.next
                    self.last=temp
                    return True
                else:
                    temp=temp.next
        
    def delete_after(self,item):
        if self.last == None:
            return "Any item not present in list.."
        if item == self.last.item and self.last.next==self.last:
            return "Any item not present after this.."
        else:
            search_item=self.search(item=item)
            if search_item:
                if search_item.next==self.last:
                    search_item.next=search_item.next.next
                    self.last=search_item
                else:
                    search_item.next=search_item.next.next
                return True
            else:
                return "Item is not present in list.."
                
                
                
                    
                    
                
                    
            
    
cll=CLL()
cll.insert_at_start(30)
cll.insert_at_start(20)
cll.insert_at_start(10)
cll.insert_at_end(40)
cll.insert_at_end(50)
cll.insert_at_end(60)
cll.insert_after(item=45,iaf_item=60)
cll.insert_at_start(70)
cll.traverse()
cll.delete_at_start()
cll.delete_at_end()
cll.delete_at_end()
cll.traverse()
cll.delete_this(item=40)
cll.traverse()
cll.delete_after(item=10)
cll.traverse()
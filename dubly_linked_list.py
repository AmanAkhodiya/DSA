class Node:
    def __init__(self,item=None,previous=None,next=None):
        self.item=item
        self.next=next
        self.previous=previous

class DLL:
    def __init__(self,head=None):
        self.head=head
    def insert_at_start(self,item):
        node=Node(item=item,next=self.head)
        if self.head:
            self.head.previous = node
        self.head=node
    def insert_at_end(self,item):
        node=Node(item=item)
        temp=self.head
        if temp is None:
            self.head=node
        while temp:
            if temp.next is not None:
                temp=temp.next
            else:
                temp.next=node
                node.previous=temp
                return True
    def search(self,item):
        temp=self.head
        while temp:
            if temp.item==item:
                return temp
            elif temp.next is None and temp.item!=item:
                print("Item is not Found in List..")
                return None
            else:
                temp=temp.next
    def insert_after(self,item,iaf_item):
        node=Node(item=item)
        iaf_node=self.search(item=iaf_item)
        if iaf_node:
            iaf_node.next.previous=node
            node.next=iaf_node.next
            iaf_node.next=node
            node.previous=iaf_node
        else:
            return False
    def traverse(self,item=None,help="Traverse after this item(optional)"):
        if item is None:
            temp=self.head
        else:
            temp=self.search(item=item)
        while temp:
            print(temp.item,end=" ")
            if temp.next is None:
                print()
                return temp
            temp=temp.next   
    def traverse_reverse(self,item=None,help="Traverse before this item(optional)"):
        if item is not None:
            temp=self.search(item=item)
        else:
            temp=self.traverse()
        while temp:
            print(temp.item,end=" ") 
            temp = temp.previous
        print()
                  
    def delete_after(self,item):
        search_item=self.search(item=item)
        if search_item:
            if search_item.next==None:
                print(f"Any item not found after:{item}")
                return False
            else:
                if search_item.next.next is not None:
                    search_item.next.next.previous=search_item
                search_item.next = search_item.next.next
                return True
                
dll=DLL()     
dll.insert_at_start(item=20)
dll.insert_at_start(item=10)
dll.insert_at_start(item=0)
dll.insert_at_end(item=30)
dll.insert_at_end(item=40)
dll.insert_at_end(item=50)
dll.insert_at_end(item=60)
dll.insert_after(item=45,iaf_item=40)
dll.traverse()
dll.delete_after(item=10)
dll.traverse()
     
                
            
        
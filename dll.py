class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class doubly_linked_list:

    def __init__(self):
        self.head = None

    def add_front(self, newval):
        newnode = Node(newval)
        newnode.next= self.head
        if self.head :
            self.head.prev=newnode
        self.head=newnode

    def add_after(self, search_value, newval):
        newnode=Node(newval)
        dll=self.head
        while dll:
            if dll.data == search_value:
                break 
            dll=dll.next
        newnode.next = dll.next
        newnode.prev=dll
        dll.next.prev = newnode
        dll.next = newnode
    
    def append_last (self, newval):
        newnode = Node(newval)
        dll = self.head
        while (dll.next):
            dll = dll.next
        dll.next=newnode
        newnode.prev=dll
    
    def delete_val(self, delval):
        dll = self.head
        while dll:
            prevVal=dll.prev
            if dll.data==delval:
                break
            dll=dll.next
        if dll.next:
            prevVal.next = dll.next
            dll.next.prev = prevVal
        else :
            prevVal.next=None

    def dll_print(self, node):
        while node :
            print (node.data)
            node = node.next
    
dllist = doubly_linked_list()
dllist.add_front(1)
dllist.add_front(2)
dllist.add_front(3)
dllist.add_front(4)
dllist.add_front(5)

dllist.add_after(3,35)

dllist.append_last(15)
dllist.delete_val(35)
dllist.delete_val(15)

dllist.dll_print(dllist.head)
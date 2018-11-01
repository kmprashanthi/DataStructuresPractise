class Node:
    def __init__(self,val=None):
        self.val=val
        self.nextval=None

class LinkedLists:
    def __init__(self):
        self.head=None

    def listprint(self):
        thislist=list1.head
        while thislist:
            print (thislist.val)
            thislist=thislist.nextval

    def insert_beg(self,new_val=None):
        newnode=Node(new_val)
        newnode.nextval=self.head
        self.head=newnode

    def insert_end(self,new_val=None):
        newnode=Node(new_val)
        #if there are no nodes 
        if self.head==None:
            self.head=newnode
        lastnode=self.head
        while lastnode.nextval:
            lastnode=lastnode.nextval
        lastnode.nextval=newnode

    def remove_node(self,remove_val):
        head_node=self.head
        #first node itself matches 
        if head_node:
            if head_node.val==remove_val:
                self.head = head_node.nextval
                head_node=None
        #for other values down the list
        while head_node:
            if head_node.val==remove_val:
                break
            prev=head_node   # has the previous node s value, coz when it matches it break s the while loop
            head_node=head_node.nextval
        if head_node == None:
            return 
        prev.nextval=head_node.nextval
        head_node=None
        

list1=LinkedLists()
list1.head=Node("Mon")
e2=Node("tues")
e3=Node("wed")

list1.head.nextval=e2
e2.nextval=e3

list1.insert_beg("Sun")
list1.insert_end("thur")
list1.remove_node("Sun")
list1.remove_node("tues")
list1.listprint()
class stack:
    def __init__(self):
        self.stack=[]
    
    def add (self,val):
        self.stack.append(val)

    def remove(self):
        if len(self.stack)<=0:
            return "no element in the stack"
        else:
            return self.stack.pop()
    
    def print_stack(self):
        print (self.stack)

stack1 = stack()
stack1.add(1)
stack1.add(2)
stack1.add(2)
stack1.add(3)
stack1.print_stack()
print ("popping")
print(stack1.remove())
print(stack1.remove())
print(stack1.remove())
print(stack1.remove())
print(stack1.remove())



            
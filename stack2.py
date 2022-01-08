#  Implement a Stack, using a Python List data structure. 

class Stack: # defining stack code
    def __init__(self):
        self.items = []

    def push(self, value): #add the methods push, pop, and size to this class
        self.items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

# instantiate an object of the Stack class named stack, then use its instance method push to add 4 items to itself. 
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# code to test the push, pop, and size methods.
print("Pass" if (stack.size() == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.size() == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")

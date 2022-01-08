#Implement a class for a singly linked list's Node:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

# Begin implementing a Queue class, with a constructor method as follows:

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self): # Add a method to return the size of the Queue:
        return self.num_nodes

# Add the enqueue method as follows:
    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            # self.head = new_node
            # self.tail = new_node
            self.head = self.tail = new_node  # Same as above two lines
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.num_nodes += 1

#Add the dequeue method as follows:
    def dequeue(self):
        if self.head is None:
            return None

        # dequeue_node = self.head.value
        dequeue_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return dequeue_node_value

# instantiate an object from the Queue class

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue(4)
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
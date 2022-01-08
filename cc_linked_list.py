class Node: # code for doubly linked list
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        

    def prepend(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        while self.head is not None:
            new_node = self.head 
            new_node.next = self.head
            
            print("Prepended new Head Node with value:" ,self.head.value)
            print("Node following Head is:" , self.head.next.value)
            return


        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        print("Prepend new Node with value:" , node.next.value)
        return
        

llist = LinkedList()
llist.prepend("First Node")
llist.prepend("First New Node")


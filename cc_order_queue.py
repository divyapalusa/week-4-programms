#  Implementing a Queue as a List
class Queue:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


# define a class named IceCreamShop .
class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops
        
            
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
            return
        elif scoops < 1 or scoops > 3:
            print("choose between 1-3 scoops.")
            return
        print("Order created!")
        order = {"customer": self.customer,
                     "flavor": self.flavor, "scoops": self.scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders.items:
            print("Customer:", order["customer"], "--Flavor:", order["flavor"], "--Scoops:", order["scoops"]) 

    def next_order(self):
        print(" Next Order Up!")
        
        order = self.orders.dequeue()
        
        print("Customer:", order["customer"], "--Flavor:", order["flavor"], "--Scoops:", order["scoops"]) 


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()

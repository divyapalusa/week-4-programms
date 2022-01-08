# In this file, declare a class and give it the name User.
# Give the User class three instance attributes: name, pin, and password.
import datetime
class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self,name):
        self.name = name
        #print("Your name has been changed to :",self.name)

    def change_pin(self,pin):
        self.pin = pin
        #print("Your pin has been changed to:", self.pin)

    def change_password(self,password):
        self.password = password
        #print("Your password has been chamged to :", self.password)

class BankUser(User):
    def __init__(self,name,pin,password):
        super().__init__(name,pin,password)
        self.balance = 0
    def show_balance(self):
       
        print(self.name, "has an account balance of:", self.balance) 
    def deposit(self,amount):
        #amount = float(input("Enter amount to Deposit:"))
        
        self.balance += amount
        
        #print(self.name, "deposited amount :",self.balance)
    def withdraw(self,amount):
        #amount = float(input("Enter amount to Withdraw:"))
        
        self.balance -= amount
        #print(self.name ,"withdraws amount:",self.balance)     

    def transfer_money(self,recipient,amount):
        print(f"You are transferring  ${amount} to {recipient .name}")
        print("Authentication is Required.")
        pin = int(input("Enter your pin :"))
       
        if pin == self.pin:
            print("Transfer Authorized.")
            print(f"Transferring  ${amount} to {recipient .name}")
            self.withdraw(amount)
            recipient.deposit(amount)
            transcation_time = datetime.datetime.now()
            print(f"money transfered at {transcation_time}") 
            return True
        
        print("Invalid Pin.Transaction cancelled.")
        return False




    def request_money(self, from_user,amount):
        print(f"You are requesting  ${amount} from {from_user.name}")
        print(" User Authentication is Required...")
        pin = int(input(f"Enter {from_user.name}'s PIN :"))
        password = input("Enter your password :")
        
        if pin == user1.pin and password == user2.password:
            print("Request Authorized.")
            
            from_user.withdraw(amount)
            self.deposit(amount) 
            print(f"{from_user.name} sent ${amount}")
            transcation_time = datetime.datetime.now()
            print(f"money transfered at {transcation_time}") 

            return True
            
        elif pin != user1.pin:
            print("Invalid Pin.Transaction cancelled.")
            return False
        elif password != user2.password:
            print("Invalid password.Transcation cancelled.")
            return False




#   """ Driver Code for Task 1 """
# user = User("Bob",1234,"password")
# print(user.name , user.pin ,user.password)


# Task-2, Write three methods for the User class
#""" Driver Code for Task 2 """
# user = User("Bob",1234,"password")
# print(user.name,user.pin,user.password)
# user.change_name("Bobby")
# user.change_pin(4321)
# user.change_password("newpassword")
# print(user.name,user.pin,user.password)

# """ Driver Code for Task 3"""
# user = BankUser("Bob",1234,"password")
# print(user.name , user.pin ,user.password,user.balance)
# """ Driver Code for Task 4"""
# user = BankUser("Bob",1234,"Password")
# user.show_balance()
# user.deposit()
# user.show_balance()
# user.withdraw()
# user.show_balance()

""" Driver Code for Task 5"""
user1 = BankUser("Bob",1234,"Password")
user2 = BankUser("Alice",5678,"alicepassword")


user1.deposit(0)
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
user2.transfer_money(user1,500)
user2.show_balance()
user1.show_balance()
user2.request_money(user1, 250)
user2.show_balance()
user1.show_balance()
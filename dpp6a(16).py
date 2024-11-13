#How do you create a class method in Python?
#○ Explain the concept of a class method and give an example
#Encapsulation is a fundamental principle of object-oriented programming (OOP) that restricts direct access to an object's internal data and allows it to be modified only through specific methods. It ensures that the inner workings of a class are hidden from the outside, making it possible to change them without affecting other parts of the program that use the class. This promotes modularity, security, and ease of maintenance.

#In Python, encapsulation is primarily achieved using access modifiers:

#Public attributes: Accessible from anywhere (e.g., self.attribute).
#Protected attributes: Intended for internal use only, but accessible from subclasses (indicated by a single underscore _attribute).
#Private attributes: Restricted to the class in which they are defined (indicated by a double underscore __attribute), which helps prevent accidental access or modification from outside the class.
#Python uses name mangling for private attributes, which makes it harder to access these attributes directly from outside the class.

#Example: Private Attributes in Python
#Here’s an example demonstrating encapsulation with a private attribute in Python:

#python
#Copy code
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # public attribute
        self.__balance = balance  # private attribute
    
    # Method to get the balance (read-only access)
    def get_balance(self):
        return self.__balance
    
    # Method to deposit money (modifies private attribute)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Example usage
account = BankAccount("Alice", 1000)
print(account.get_balance())  # Accessing the private attribute through a method
account.deposit(500)          # Deposits money, modifying the private attribute
account.withdraw(300)         # Withdraws money, modifying the private attribute

# Direct access to __balance will raise an error
# print(account.__balance)  # This will raise an AttributeError

# However, name mangling allows access (not recommended)
print(account._BankAccount__balance)  # Accessing the private attribute (not recommended)

# Base class representing a generic Bank Account
class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number   # Protected attribute
        self._balance = balance                 # Protected attribute

    # Encapsulated method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    # Encapsulated method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount.")

    # Method to display balance
    def display_balance(self):
        print(f"Account {self._account_number} balance: ${self._balance}")

# Derived class representing a Savings Account with additional functionality
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)   # Inherit from BankAccount
        self._interest_rate = interest_rate         # Specific attribute for SavingsAccount

    # Polymorphism: adding interest to the balance (specific to SavingsAccount)
    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interest of ${interest} applied. New balance: ${self._balance}")

# Derived class representing a Checking Account with additional functionality
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)   # Inherit from BankAccount
        self._overdraft_limit = overdraft_limit     # Specific attribute for CheckingAccount

    # Overridden withdraw method (polymorphism) to allow overdraft
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Withdrawal amount exceeds overdraft limit.")

# Demonstrating encapsulation, inheritance, and polymorphism

# Creating a Savings Account
savings = SavingsAccount(account_number="S123", balance=1000)
savings.deposit(200)
savings.apply_interest()  # Polymorphic behavior specific to SavingsAccount
savings.display_balance()

print("\n")

# Creating a Checking Account
checking = CheckingAccount(account_number="C456", balance=500)
checking.deposit(100)
checking.withdraw(600)    # Polymorphic behavior specific to CheckingAccount with overdraft
checking.display_balance()

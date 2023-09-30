#.bank account

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        elif amount > self.__balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than zero.")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Current Balance: ${self.__balance}")


# Create an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
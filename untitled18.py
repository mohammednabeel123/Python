#Banking system
print(input("Enter your user name: "))
print(input("Enter your passowrd: "))

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into {self.account_holder}'s account.")
            self.check_balance()
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.account_holder}'s account.")
            self.check_balance()
        elif amount <= 0:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
        else:
            print("Insufficient funds. Withdrawal amount exceeds account balance.")

# Example Usage
user_account = BankAccount("John Doe", 1000)


user_account.check_balance()  # Check initial balance

user_account.deposit(500)     # Deposit money
user_account.withdraw(200)    # Withdraw money

user_account.check_balance()  # Check updated balance
    


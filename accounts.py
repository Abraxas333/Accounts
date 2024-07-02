import random
import csv
class Account:
    instances = []

    def __init__(self, account_no, owner, balance):
        self.account_no = account_no
        self.owner = owner
        self.balance = balance
        self.history = []
        Account.instances.append(self)

    def __str__(self):
        return f'{self.account_no}, {self.owner}, {self.balance}'

    def add_account(owner, balance):
            account_no = random.randint(1, 100000)
            account = Account(account_no, owner, balance)
            print(f"Account: {account.account_no}, {account.owner} added.")
            return account


    
    @staticmethod
    def del_account(owner):
        for instance in Account.instances:
            if instance.owner == owner:
                Account.instances.remove(instance)
                print(f"Account {owner} deleted successfully.")
                return
        print(f"Account {account_no} not found.")


    @staticmethod
    def find_account(owner):
        for instance in Account.instances:
            if instance.owner == owner:
                return instance
        print(f"Account {account_no} not found.")
        return None

    def return_fullinfo(self):
        return vars(self)

    def add_balance(self, amount):
        self.balance += amount
        booking = f'add {amount}'
        self.history.append(booking)



    def subtract_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            booking = f'subtract {amount}'
            self.history.append(booking)
        else:
            print("Insufficient funds.")

    @staticmethod
    def save_accounts(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            for accounts in Account.instances:
                    writer.writerow([Account.owner, Account.account_no, Account.add_balance])
                    return account
    
    def import_accounts(filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    account_no, owner, balance = row
                    Account.instances.append(Account(account_no, owner, balance))
        return Account.instances
    
    @staticmethod
    def print_accounts():
        accounts_str = ""
        for instance in Account.instances:
            accounts_str += str(instance) + "\n"
        return accounts_str
# Example usage:
# Create an account
account = Account.add_account('Wilson', 1000)

# Find the account by account number and add/subtract balance
account_no = account.account_no  # Assume we know the account number
account_to_update = Account.find_account(account_no)

if account_to_update:
    account_to_update.add_balance(100)
    account_to_update.subtract_balance(50)

# Print all accounts
Account.print_accounts()

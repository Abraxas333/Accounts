import csv
import uuid

class Account:
    instances = []

    def __init__(self, account_no, owner, balance):
        self.account_no = account_no
        self.owner = owner
        self.balance = balance
        self.history = []
        Account.instances.append(self)

    def __str__(self):
        return f'Account No: {self.account_no}, Owner: {self.owner}, Balance: {self.balance}'

    @classmethod
    def add_account(cls, owner, balance):
        # Validation for owner
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner must be a non-empty string.")
        
        # Validation for balance
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a non-negative number.")
        
        # Generate a unique account number
        account_no = str(uuid.uuid4())
        account = cls(account_no, owner, balance)
        print(f"Account: {account.account_no}, {account.owner} added.")
        return account

    @classmethod
    def del_account(cls, owner):
        for instance in cls.instances:
            if instance.owner == owner:
                cls.instances.remove(instance)
                print(f"Account {owner} deleted successfully.")
                return
        print(f"Account {owner} not found.")

    @classmethod
    def find_account(cls, owner):
        for instance in cls.instances:
            if instance.owner == owner:
                return instance
        print(f"Account {owner} not found.")
        return None

    def add_balance(self, amount):
        self.balance += amount
        self.history.append(f'add {amount}')

    def subtract_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f'subtract {amount}')
        else:
            print("Insufficient funds.")

    @classmethod
    def save_accounts(cls, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for account in cls.instances:
                writer.writerow([account.account_no, account.owner, account.balance])

    @classmethod
    def import_accounts(cls, filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    account_no, owner, balance = row
                    cls(account_no, owner, float(balance))
        return cls.instances

    @classmethod
    def export_accounts(cls, filename):
        with open(filename, 'w', newline='') as file:  # Changed to 'w' mode to overwrite the file
            writer = csv.writer(file)
            for account in cls.instances:
                writer.writerow([account.account_no, account.owner, account.balance])

    @classmethod
    def print_accounts(cls):
        accounts_str = ""
        for instance in cls.instances:
            accounts_str += str(instance) + "\n"
        return accounts_str

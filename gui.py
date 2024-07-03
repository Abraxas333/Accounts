import tkinter as tk
from tkinter import messagebox, ttk
from accounts import Account

root = tk.Tk()
root.title("Account Manager")
root.geometry("700x472")

# Import list of accounts
file = r'./output'
Account.import_accounts(file)

def button_add():
    try:
        owner_balance_input = add_account_entry.get().split()
        if len(owner_balance_input) != 2:
            raise ValueError("Input should be '<owner> <balance>'.")
        owner = owner_balance_input[0].lower().strip()
        balance = float(owner_balance_input[1])
        account = Account.add_account(owner, balance)
        messagebox.showinfo("Success", f"Account added:\n{account}")
        add_account_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add account due to {e}.")

def button_del():
    try:
        account_owner = del_account_entry.get().lower().strip()
        Account.del_account(account_owner)
        messagebox.showinfo("Success", f"Account {account_owner} deleted successfully.")
        del_account_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete account due to {e}.")

def button_print_accounts():
    try:
        accounts_info = Account.print_accounts()
        messagebox.showinfo("All Accounts", accounts_info)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to print accounts due to {e}")

def add_balance():
    try:
        owner_amount_input = deposit_entry.get().split()
        if len(owner_amount_input) != 2:
            raise ValueError("Invalid input format. Should be '<owner> <amount>'.")
        owner = owner_amount_input[0].lower().strip()
        amount = float(owner_amount_input[1])
        account = Account.find_account(owner)
        if account:
            account.add_balance(amount)
            messagebox.showinfo("Success", f"Deposited {amount} to account {owner}.")
            deposit_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Account {owner} not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to deposit due to {e}.")

def withdraw_balance():
    try:
        owner_amount_input = withdraw_entry.get().split()
        if len(owner_amount_input) != 2:
            raise ValueError("Invalid input format. Should be '<owner> <amount>'.")
        owner = owner_amount_input[0].lower().strip()
        amount = float(owner_amount_input[1])
        account = Account.find_account(owner)
        if account:
            if account.balance >= amount:
                account.subtract_balance(amount)
                messagebox.showinfo("Success", f"Withdrew {amount} from account {owner}.")
                withdraw_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        else:
            messagebox.showerror("Error", f"Account {owner} not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to withdraw due to {e}.")

def accounts_import_export():
    filename = file_entry.get().strip()
    action = value_inside.get()
    try:
        if action == 'import':
            Account.import_accounts(filename)
            accounts_info = Account.print_accounts()
            messagebox.showinfo("Success", f"Imported accounts:\n{accounts_info}")
            file_entry.delete(0, tk.END)
        elif action == 'export':
            Account.export_accounts(filename)
            messagebox.showinfo("Success", "Accounts exported")
            file_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to {action} accounts due to {e}.")

def check_balance():
    try:
        owner = check_balance_entry.get().lower().strip()
        account = Account.find_account(owner)
        if account:
            messagebox.showinfo("Success", str(account))
        else:
            messagebox.showerror("Error", f"Account {owner} not found.")
        check_balance_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to find Account {owner} due to {e}")

# GUI Layout

# Add account
button_add_account_label = ttk.Label(root, text="Add account")
button_add_account_label.grid(row=1, column=0, padx=15, pady=10)
button_add_account = ttk.Button(root, text="Add", command=button_add)
button_add_account.grid(row=1, column=2, padx=1, pady=10)
add_account_entry = ttk.Entry(root, width=35)
add_account_entry.grid(row=1, column=1, padx=5, pady=5)

# Delete account
button_del_account_label = ttk.Label(root, text="Delete account")
button_del_account_label.grid(row=2, column=0, padx=15, pady=10)
button_del_account = ttk.Button(root, text="Delete", command=button_del)
button_del_account.grid(row=2, column=2, padx=10, pady=10)
del_account_entry = ttk.Entry(root, width=35)
del_account_entry.grid(row=2, column=1, padx=5, pady=5)

# Check balance
button_check_balance_label = ttk.Label(root, text="Check balance")
button_check_balance_label.grid(row=3, column=0, padx=10, pady=10)
button_check_balance = ttk.Button(root, text="Check", command=check_balance)
button_check_balance.grid(row=3, column=2, padx=15, pady=10)
check_balance_entry = ttk.Entry(root, width=35)
check_balance_entry.grid(row=3, column=1, padx=5, pady=5)

# Deposit
button_deposit_label = ttk.Label(root, text="Deposit")
button_deposit_label.grid(row=6, column=0, padx=15, pady=10)
deposit_entry = ttk.Entry(root, width=35)
deposit_entry.grid(row=6, column=1, padx=5, pady=5)
button_deposit = ttk.Button(root, text="OK", command=add_balance)
button_deposit.grid(row=6, column=2, padx=15, pady=10)

# Withdraw
button_withdraw_label = ttk.Label(root, text="Withdraw")
button_withdraw_label.grid(row=7, column=0, padx=15, pady=10)
withdraw_entry = ttk.Entry(root, width=35)
withdraw_entry.grid(row=7, column=1, padx=5, pady=5)
button_withdraw = ttk.Button(root, text="OK", command=withdraw_balance)
button_withdraw.grid(row=7, column=2, padx=15, pady=10)

# options menu for add, del, check, withdraw, deposit
value_option = tk.StringVar(root)
value_option.set("Select an Option")
options_account = ["add", "check", "del", "deposit", "withdraw" ]
options_menu = tk.OptionMenu(root, value_option, *options_account)
options_menu.grid(row=13, column= 1)
# File location
file_label = ttk.Label(root, text="File location:")
file_label.grid(row=10, column=0, padx=5, pady=5)
file_entry = ttk.Entry(root, width=35)
file_entry.grid(row=10, column=1, padx=5, pady=5)

# Import/export options
value_inside = tk.StringVar(root)
value_inside.set("Select an Option")
options_list = ["import", "export"]
question_menu = tk.OptionMenu(root, value_inside, *options_list)
question_menu.grid(row=9, column=1, padx=5, pady=5)
button_import_export = ttk.Button(root, text="OK", command=accounts_import_export)
button_import_export.grid(row=10, column=2)

# Print all accounts
button_print_account_label = ttk.Label(root, text="Print all accounts")
button_print_account_label.grid(row=11, column=0, padx=15, pady=10)
button_print_account = ttk.Button(root, text="Print", command=button_print_accounts)
button_print_account.grid(row=11, column=2, padx=1, pady=10)

root.mainloop()

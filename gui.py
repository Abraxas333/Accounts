import tkinter as tk
from tkinter import messagebox, ttk, Button
from accounts import Account
import re

# Initialize main window
root = tk.Tk()
root.title("Account Manager")
root.geometry("728x450")
root.configure(bg='#f0f0f0')

# Set the theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

# center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# Import list of accounts
file = './output'
Account.import_accounts(file)

# input validation functions
def validate_owner(owner):
    return owner.isalpha() and owner != ""

def validate_balance(balance):
    try:
        balance = float(balance)
        return balance >= 0
    except ValueError:
        return False

def validate_filename(filename):
    return re.match(r'^[\w\-. ]+$', filename) is not None and filename != ""

# Button functions
def button_add():
    try:
        owner = owner_entry.get().lower().strip()
        balance = balance_entry.get().strip()
        if validate_owner(owner) and validate_balance(balance):
            account = Account.add_account(owner, float(balance))
            messagebox.showinfo("Success", f"Account added:\n{account}")
            owner_entry.delete(0, tk.END)
            balance_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid input. Ensure the owner is alphabetic, not empty, and balance is a non-negative numeric value.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add account due to {e}.")

def button_del():
    try:
        account_owner = owner_entry.get().lower().strip()
        if validate_owner(account_owner):
            Account.del_account(account_owner)
            messagebox.showinfo("Success", f"Account {account_owner} deleted successfully.")
            owner_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid input. Ensure the owner is alphabetic and not empty.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete account due to {e}.")

def add_balance():
    try:
        owner = owner_entry.get().lower().strip()
        amount = balance_entry.get().strip()
        if validate_owner(owner) and validate_balance(amount):
            account = Account.find_account(owner)
            if account:
                account.add_balance(float(amount))
                messagebox.showinfo("Success", f"Deposited {amount} to account {owner}.")
                owner_entry.delete(0, tk.END)
                balance_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"Account {owner} not found.")
        else:
            messagebox.showerror("Error", "Invalid input. Ensure the owner is alphabetic, not empty, and amount is a non-negative numeric value.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to deposit due to {e}.")

def withdraw_balance():
    try:
        owner = owner_entry.get().lower().strip()
        amount = balance_entry.get().strip()
        if validate_owner(owner) and validate_balance(amount):
            account = Account.find_account(owner)
            if account:
                if account.balance >= float(amount):
                    account.subtract_balance(float(amount))
                    messagebox.showinfo("Success", f"Withdrew {amount} from account {owner}.")
                    owner_entry.delete(0, tk.END)
                    balance_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Insufficient funds.")
            else:
                messagebox.showerror("Error", f"Account {owner} not found.")
        else:
            messagebox.showerror("Error", "Invalid input. Ensure the owner is alphabetic, not empty, and amount is a non-negative numeric value.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to withdraw due to {e}.")

def check_balance():
    try:
        owner = owner_entry.get().lower().strip()
        if validate_owner(owner):
            account = Account.find_account(owner)
            if account:
                messagebox.showinfo("Success", str(account))
            else:
                messagebox.showerror("Error", f"Account {owner} not found.")
            owner_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid input. Ensure the owner is alphabetic and not empty.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to find Account {owner} due to {e}")

def execute_selected_action():
    action = action_var.get()
    if action == "Add Account":
        button_add()
    elif action == "Delete Account":
        button_del()
    elif action == "Deposit":
        add_balance()
    elif action == "Withdraw":
        withdraw_balance()
    elif action == "Check Balance":
        check_balance()

def accounts_import_export():
    filename = file_entry.get().strip()
    action = import_export_var.get()
    try:
        if validate_filename(filename):
            if action == 'import':
                Account.import_accounts(filename)
                accounts_info = Account.print_accounts()
                messagebox.showinfo("Success", f"Imported accounts:\n{accounts_info}")
                file_entry.delete(0, tk.END)
            elif action == 'export':
                Account.export_accounts(filename)
                messagebox.showinfo("Success", "Accounts exported")
                file_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid file name. Ensure the filename contains only alphanumeric characters, underscores, hyphens, periods, and spaces, and is not empty.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to {action} accounts due to {e}.")

def button_print_accounts():
    try:
        accounts_info = Account.print_accounts()
        messagebox.showinfo("All Accounts", accounts_info)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to print accounts due to {e}")

# style for label, button, etries
style = ttk.Style()
style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))

# frames to center the content
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky="nsew")
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(0, weight=4)  
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_rowconfigure(5, weight=3)
frame.grid_rowconfigure(6, weight=1)
frame.grid_rowconfigure(7, weight=1)
frame.grid_rowconfigure(8, weight=1)
frame.grid_rowconfigure(9, weight=1)
frame.grid_rowconfigure(10, weight=1) 
frame.grid_rowconfigure(11, weight=4) 

# combobox menu for actions
actions = ["Add Account", "Delete Account", "Deposit", "Withdraw", "Check Balance"]
action_var = tk.StringVar(root)
action_var.set(actions[0])
action_menu = ttk.Combobox(frame, textvariable=action_var, values=actions, state='readonly', width=30)
action_menu.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Execute button for dropdown menu
execute_button = ttk.Button(frame, text="Execute", command=execute_selected_action)
execute_button.grid(row=4, column=1, padx=10, pady=0, sticky=tk.W)

# Owner input field
owner_label = ttk.Label(frame, text="Owner:")
owner_label.grid(row=2, column=0, padx=0, pady=5, sticky=tk.E)
owner_entry = ttk.Entry(frame, width=22)
owner_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W)

# Balance input field
balance_label = ttk.Label(frame, text="Amount:")
balance_label.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)
balance_entry = ttk.Entry(frame, width=10)
balance_entry.grid(row=2, column=2, padx=5, pady=0, columnspan=2, sticky=tk.W)

# File location
file_label = ttk.Label(frame, text="File location:")
file_label.grid(row=7, column=0, padx=0, pady=5, sticky=tk.E)
file_entry = ttk.Entry(frame, width=35)
file_entry.grid(row=7, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W)

# Dropdown for import/export
import_export_options = ["import", "export"]
import_export_var = tk.StringVar(root)
import_export_var.set(import_export_options[0])
import_export_menu = ttk.Combobox(frame, textvariable=import_export_var, values=import_export_options, state='readonly', width=30)
import_export_menu.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

# Import/export button
import_export_button = ttk.Button(frame, text="OK", command=accounts_import_export)
import_export_button.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)

# Print all accounts button
button_print_account = ttk.Button(frame, text="Print All Accounts", command=button_print_accounts)
button_print_account.grid(row=9, column=1, pady=5, padx=10, columnspan=2, sticky=tk.W)

# End button
button_end = ttk.Button(frame, text="End", command=root.quit)
button_end.grid(row=10, column=1, pady=0, padx=10, columnspan=2, sticky=tk.W)

root.mainloop()

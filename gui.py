import tkinter as tk
from tkinter import messagebox, ttk
from accounts import Account



def button_add():
    try:
        owner_balance_input = add_account_entry.get().split()
        owner = owner_balance_input[0]
        balance = float(owner_balance_input[1])
        account = Account.add_account(owner, balance)
        messagebox.showinfo("Success", f"Account added:\n{account}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add account due to {e}.")

def button_del():
    try:
        account_no_to_del = del_account_entry.get()
        Account.del_account(account_no_to_del)
        messagebox.showinfo("Success", f"Account {account_no_to_del} deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete account due to {e}.")

def button_print_accounts():
    try:
        accounts_info = Account.print_accounts()
        messagebox.showinfo("All Accounts", accounts_info)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to print accounts due to {e}")

def accounts_import_export(filename, action):
    try:
        if action == 'import':
            Account.import_accounts(filename)
            accounts = Account.instances
            accounts_info = "\n".join(
                [f"Account: {Account.account_no}, {Account.owner}, {Account.add_balance}"])
            messagebox.showinfo("Success", f"Imported members:\n{accounts_info}")
    
    except Exception as e:
        pass
# main gui
root = tk.Tk()
root.title("account manager")
root.geometry("700x472")

# anlegen von Konten
button_add_account_label = ttk.Label(root, text="add account")
button_add_account_label.grid(row=1, column=0, padx=15, pady=10)

button_add_account = ttk.Button(root, text="add", command=button_add)
button_add_account.grid(row=1, column=2, padx=1, pady=10)

add_account_entry = ttk.Entry(root, width=35)
add_account_entry.grid(row=1, column=1, padx=5, pady=5)

# löschen von Konten
button_del_account_label = ttk.Label(root, text="del account")
button_del_account_label.grid(row=2, column=0, padx=15, pady=10)

button_del_account = ttk.Button(root, text="del", command=button_del)
button_del_account.grid(row=2, column=2, padx=10, pady=10)

del_account_entry = ttk.Entry(root, width=35)
del_account_entry.grid(row=2, column=1, padx=5, pady=5)

# kontostand berechnen
button_check_balance_label = ttk.Label(root, text="check balance")
button_check_balance_label.grid(row=3, column=0, padx=10, pady=10)

button_check_balance = ttk.Button(root, text="check")
button_check_balance.grid(row=3, column=2, padx=15, pady=10)

check_balance_entry = ttk.Entry(root, width=35)
check_balance_entry.grid(row=3, column=1, padx=5, pady=5)

# geld beheben
button_withdraw_label = ttk.Label(root, text="withdraw")
button_withdraw_label.grid(row=4, column=0, padx=15, pady=10)

withdraw_entry = ttk.Entry(root, width=35)
withdraw_entry.grid(row=4, column=1, padx=5, pady=5)

button_withdraw = ttk.Button(root, text="OK")
button_withdraw.grid(row=4, column=2, padx=15, pady=10)

# geld einzahlen 
button_deposit_label = ttk.Label(root, text="deposit")
button_deposit_label.grid(row=6, column=0, padx=15, pady=10)

deposit_entry = ttk.Entry(root, width=35)
deposit_entry.grid(row=6, column=1, padx=5, pady=5)

button_deposit = ttk.Button(root, text="OK")
button_deposit.grid(row=6, column=2, padx=15, pady=10)

# alle Konten auslesen
button_print_account_label = ttk.Label(root, text="print all accounts")
button_print_account_label.grid(row=7, column=0, padx=15, pady=10)

button_print_account = ttk.Button(root, text="print", command=button_print_accounts)
button_print_account.grid(row=7, column=2, padx=1, pady=10)
# datenausgabe einzelenes Konto 

button_import_export_label = ttk.Label(root, text="import/export")
button_import_export_label.grid(row=9, column=0, padx=15, pady=10)

button_import_export= ttk.Button(root, text="OK", command=accounts_import_export)
button_import_export.grid(row=10, column=2)


options_list = ["import", "export",] 

value_inside = tk.StringVar(root)
value_inside.set("Select an Option")
action = value_inside
question_menu = tk.OptionMenu(root, value_inside, *options_list) 
question_menu.grid(row=9, column=1, padx=5, pady=5)

file_label = ttk.Label(root, text="File location:")
file_label.grid(row=10, column=0, padx=5, pady=5)
file_entry = ttk.Entry(root, width=35)
file_entry.grid(row=10, column=1, padx=5, pady=5)

root.mainloop()
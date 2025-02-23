import tkinter as tk
from tkinter import messagebox

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}"  

class BankingSystem:
    def __init__(self, root):
        self.accounts = {}

        self.root = root
        self.root.title("Banking System")
        self.root.geometry("700x600")  
        self.root.config(bg="#F4F6F9")  

        self.create_widgets()

    def create_widgets(self):
        self.create_account_section()
        self.transaction_section()
        self.account_info_section()

    def create_account_section(self):
        self.create_account_frame = tk.LabelFrame(self.root, text="Create Account", bg="#FFFFFF", font=("Arial", 14), padx=20, pady=20)
        self.create_account_frame.pack(pady=10, padx=20, fill="x")

        self.acc_num_entry, self.acc_holder_entry, self.initial_balance_entry = self.create_entries(self.create_account_frame, ["Account Number:", "Account Holder:", "Initial Balance:"])
        self.create_acc_button = tk.Button(self.create_account_frame, text="Create Account", command=self.create_account, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", bd=3)
        self.create_acc_button.pack(pady=10)
    
    def transaction_section(self):
        self.transaction_frame = tk.LabelFrame(self.root, text="Transactions", bg="#FFFFFF", font=("Arial", 14), padx=20, pady=20)
        self.transaction_frame.pack(pady=10, padx=20, fill="x")

        self.trans_acc_num_entry, self.amount_entry = self.create_entries(self.transaction_frame, ["Account Number:", "Amount:"])
        
        button_frame = tk.Frame(self.transaction_frame, bg="#FFFFFF")
        button_frame.pack(pady=10)
        
        self.deposit_button = tk.Button(button_frame, text="Deposit", command=self.deposit, font=("Arial", 14), bg="#2196F3", fg="white", relief="raised", bd=3)
        self.deposit_button.grid(row=0, column=0, padx=5)

        self.withdraw_button = tk.Button(button_frame, text="Withdraw", command=self.withdraw, font=("Arial", 14), bg="#F44336", fg="white", relief="raised", bd=3)
        self.withdraw_button.grid(row=0, column=1, padx=5)
    
    def account_info_section(self):
        self.info_frame = tk.LabelFrame(self.root, text="Account Information", bg="#FFFFFF", font=("Arial", 14), padx=20, pady=20)
        self.info_frame.pack(pady=10, padx=20, fill="x")

        self.info_acc_num_entry = self.create_entry(self.info_frame, "Account Number:")
        self.info_button = tk.Button(self.info_frame, text="Display Info", command=self.display_info, font=("Arial", 14), bg="#FFC107", fg="white", relief="raised", bd=3)
        self.info_button.pack(pady=10)
    
    def create_entries(self, parent, labels):
        entries = []
        for label in labels:
            frame = tk.Frame(parent, bg="#FFFFFF")
            frame.pack(fill="x", pady=5)
            tk.Label(frame, text=label, bg="#FFFFFF", font=("Arial", 12)).pack(side="left", padx=10)
            entry = tk.Entry(frame, font=("Arial", 12), relief="sunken", bd=2)
            entry.pack(side="right", fill="x", expand=True, padx=10)
            entries.append(entry)
        return entries

    def create_entry(self, parent, label):
        frame = tk.Frame(parent, bg="#FFFFFF")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text=label, bg="#FFFFFF", font=("Arial", 12)).pack(side="left", padx=10)
        entry = tk.Entry(frame, font=("Arial", 12), relief="sunken", bd=2)
        entry.pack(side="right", fill="x", expand=True, padx=10)
        return entry

    def create_account(self):
        acc_num, acc_holder, initial_balance = self.acc_num_entry.get(), self.acc_holder_entry.get(), self.initial_balance_entry.get()
        
        if not acc_num or not acc_holder or not initial_balance.isdigit():
            messagebox.showwarning("Error", "Please fill in all fields correctly!")
            return
        
        self.accounts[acc_num] = Account(acc_num, acc_holder, float(initial_balance))
        messagebox.showinfo("Success", "Account created successfully!")

    def deposit(self):
        acc_num, amount = self.trans_acc_num_entry.get(), self.amount_entry.get()
        
        if acc_num in self.accounts and amount.isdigit():
            self.accounts[acc_num].deposit(float(amount))
            messagebox.showinfo("Success", f"Deposited {amount}. New balance: {self.accounts[acc_num].get_balance()}.")
        else:
            messagebox.showwarning("Error", "Invalid account or amount!")
    
    def withdraw(self):
        acc_num, amount = self.trans_acc_num_entry.get(), self.amount_entry.get()
        
        if acc_num in self.accounts and amount.isdigit():
            try:
                self.accounts[acc_num].withdraw(float(amount))
                messagebox.showinfo("Success", f"Withdrew {amount}. New balance: {self.accounts[acc_num].get_balance()}.")
            except InsufficientFundsError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Invalid account or amount!")

    def display_info(self):
        acc_num = self.info_acc_num_entry.get()
        if acc_num in self.accounts:
            messagebox.showinfo("Account Info", self.accounts[acc_num].display_account_info())
        else:
            messagebox.showwarning("Error", "Account not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()

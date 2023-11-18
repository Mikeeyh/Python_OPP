import tkinter as tk
from tkinter import simpledialog, messagebox
from account import Account


class BankApp:
    def __init__(self, master):
        self.master = master
        master.title("Bank Application")

        self.account = Account("John Doe", 1000)

        self.balance_label = tk.Label(master, text=f"Balance: {self.account.balance}")
        self.balance_label.pack()

        self.deposit_button = tk.Button(master, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

    def deposit(self):
        deposit_amount = simpledialog.askinteger("Deposit", "Enter deposit amount:")
        if deposit_amount is not None:
            self.account.add_transaction(deposit_amount)
            self.update_balance()

    def withdraw(self):
        withdraw_amount = simpledialog.askinteger("Withdraw", "Enter withdrawal amount:")
        if withdraw_amount is not None:
            try:
                self.account.handle_transaction(withdraw_amount)
                self.update_balance()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def update_balance(self):
        self.balance_label.config(text=f"Balance: {self.account.balance}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()

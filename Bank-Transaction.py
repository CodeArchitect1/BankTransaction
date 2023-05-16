
import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance')
            return self.balance 
        else:
            self.balance -= amount
            return self.balance


class BankUser:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None
class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Bank Management')
        self.users = []

        # Create a Frame for User operations
        self.user_frame = tk.Frame(self.root)
        self.user_frame.pack()

        self.user_label = tk.Label(self.user_frame, text='User Name:')
        self.user_label.pack(side='left')

        self.user_entry = tk.Entry(self.user_frame)
        self.user_entry.pack(side='left')

        self.user_button = tk.Button(self.user_frame, text='Create User', command=self.create_user)
        self.user_button.pack(side='left')

        # Create a Frame for Account operations
        self.account_frame = tk.Frame(self.root)
        self.account_frame.pack()

        self.account_label = tk.Label(self.account_frame, text='Account Name:')
        self.account_label.pack(side='left')

        self.account_entry = tk.Entry(self.account_frame)
        self.account_entry.pack(side='left')

        self.account_button = tk.Button(self.account_frame, text='Create Account', command=self.create_account)
        self.account_button.pack(side='left')

        # Create a Frame for Transaction operations
        self.transaction_frame = tk.Frame(self.root)
        self.transaction_frame.pack()

        self.amount_label = tk.Label(self.transaction_frame, text='Amount:')
        self.amount_label.pack(side='left')

        self.amount_entry = tk.Entry(self.transaction_frame)
        self.amount_entry.pack(side='left')

        self.deposit_button = tk.Button(self.transaction_frame, text='Deposit', command=self.deposit)
        self.deposit_button.pack(side='left')

        self.withdraw_button = tk.Button(self.transaction_frame, text='Withdraw', command=self.withdraw)
        self.withdraw_button.pack(side='left')

        self.balance_button = tk.Button(self.transaction_frame, text='Check Balance', command=self.check_balance)
        self.balance_button.pack(side='left')

    def create_user(self):
        name = self.user_entry.get()
        user = BankUser(name)
        self.users.append(user)
        messagebox.showinfo('Info', f'User {name} created.')
        self.user_entry.delete(0, 'end')  # clear the entry field


    def create_account(self):
        user_name = self.user_entry.get()
        account_name = self.account_entry.get()
        user = next((user for user in self.users if user.name == user_name), None)
        if user:
            account = BankAccount(account_name)
            user.add_account(account)
            messagebox.showinfo('Info', f'Account {account_name} created.')
            self.account_entry.delete(0, 'end')  # clear the entry field
        else:
            messagebox.showerror('Error', 'User not found')
            # ... (get the current user, create a new BankAccount, and add it to the user)

    def deposit(self):
        user_name = self.user_entry.get()
        account_name = self.account_entry.get()
        amount = float(self.amount_entry.get())
        user = next((user for user in self.users if user.name == user_name), None)
        if user:
            account = user.get_account(account_name)
            if account:
                account.deposit(amount)
                messagebox.showinfo('Info', f'Balance after deposit: {account.balance}')
                self.amount_entry.delete(0, 'end')  # clear the entry field
            else:
                messagebox.showerror('Error', 'Account not found')
        else:
            messagebox.showerror('Error', 'User not found')
                # ... (get the current user and account, and deposit the entered amount)

    def withdraw(self):
        user_name = self.user_entry.get()
        account_name = self.account_entry.get()
        amount = float(self.amount_entry.get())
        user = next((user for user in self.users if user.name == user_name), None)
        if user:
            account = user.get_account(account_name)
            if account:
                initial_balance = account.balance
                final_balance = account.withdraw(amount)
                if initial_balance == final_balance:
                    messagebox.showinfo('Info', 'Insufficient balance')
                else:
                    messagebox.showinfo('Info', f'Balance after withdrawal: {final_balance}')
                self.amount_entry.delete(0, 'end')  # clear the entry field
            else:
                messagebox.showerror('Error', 'Account not found')
        else:
            messagebox.showerror('Error', 'User not found')

    def check_balance(self):
        user_name = self.user_entry.get()
        account_name = self.account_entry.get()
        user = next((user for user in self.users if user.name == user_name), None)
        if user:
            account = user.get_account(account_name)
            if account:
                messagebox.showinfo('Info', f'Current balance: {account.balance}')
            else:
                messagebox.showerror('Error', 'Account not found')
        else:
            messagebox.showerror('Error', 'User not found')
                # ... (get the current user and account, and display the balance)

def main_console():
    users = []

    while True:
        print('1: Create User\n2: Access User\n3: Quit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            name = input('Enter user name: ')
            user = BankUser(name)
            users.append(user)
            print(f'User {name} created.')

        elif choice == 2:
            name = input('Enter user name: ')
            user = next((user for user in users if user.name == name), None)

            if user:
                while True:
                    print('1: Create Account\n2: Access Account\n3: Go Back')
                    choice = int(input('Enter your choice: '))

                    if choice == 1:
                        name = input('Enter account name: ')
                        account = BankAccount(name)
                        user.add_account(account)
                        print(f'Account {name} created.')

                    elif choice == 2:
                        name = input('Enter account name: ')
                        account = user.get_account(name)

                        if account:
                            while True:
                                print('1: Deposit\n2: Withdraw\n3: Check Balance\n4: Go Back')
                                choice = int(input('Enter your choice: '))

                                if choice == 1:
                                    amount = float(input('Enter amount to deposit: '))
                                    print(f'Balance after deposit: {account.deposit(amount)}')
                                elif choice == 2:
                                    amount = float(input('Enter amount to withdraw: '))
                                    print(f'Balance after withdrawal: {account.withdraw(amount)}')
                                elif choice == 3:
                                    print(f'Current balance: {account.balance}')
                                elif choice == 4:
                                    break
                                else:
                                    print('Invalid choice')
                        else:
                            print('Account not found')

                    elif choice == 3:
                        break
                    else:
                        print('Invalid choice')
            else:
                print('User not found')

        elif choice == 3:
            break
        else:
            print('Invalid choice')
def main_gui():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

def choose_interface():
    print('1: GUI\n2: Console\n3: Quit')
    choice = int(input('Enter your choice: '))
    return choice


if __name__ == '__main__':
    choice = choose_interface()
    if choice == 1:
        main_gui()
    elif choice == 2:
        main_console()
    elif choice == 3:
        exit()
    else:
        print('Invalid choice')

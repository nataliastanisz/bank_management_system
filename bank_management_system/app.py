import json
import os

class BankSystem:
    def __init__(self):
        self.data_file = "bank_database.json"
        self.accounts = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.accounts = json.load(file)

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.accounts, file, indent=4)

    def create_account(self):
        name = input("Enter your full name: ")
        if name in self.accounts:
            print("An account with this name already exists!")
            return

        pin = input("Set a 4-digit PIN: ")
        
        try:
            deposit = float(input("How much money do you want to deposit to start? $"))
        except ValueError:
            print("Error! You must enter a valid number. Please try again.")
            return

        self.accounts[name] = {"pin": pin, "balance": deposit}
        self.save_data()
        print(f"Success! Account created for: {name} with an initial balance of ${deposit}.")

    def deposit_money(self):
        name = input("Enter your full name: ")
        if name not in self.accounts:
            print("Error: Account not found.")
            return
        
        try:
            amount = float(input("Enter the amount to deposit: $"))
            if amount <= 0:
                print("The deposit amount must be greater than 0!")
                return
        except ValueError:
            print("Error! Please enter a valid number.")
            return

        self.accounts[name]["balance"] += amount
        self.save_data()
        print(f"Success! Deposited ${amount}. New balance: ${self.accounts[name]['balance']}.")

    def withdraw_money(self):
        name = input("Enter your full name: ")
        if name not in self.accounts:
            print("Error: Account not found.")
            return
        
        pin = input("Enter your PIN: ")
        if self.accounts[name]["pin"] != pin:
            print("Error: Invalid PIN!")
            return

        try:
            amount = float(input("Enter the amount to withdraw: $"))
        except ValueError:
            print("Error! Please enter a valid number.")
            return

        if amount > self.accounts[name]["balance"]:
            print("Error: Insufficient funds in the account.")
        elif amount <= 0:
            print("The withdrawal amount must be greater than 0!")
        else:
            self.accounts[name]["balance"] -= amount
            self.save_data()
            print(f"Success! Withdrew ${amount}. New balance: ${self.accounts[name]['balance']}.")

    def check_balance(self):
        name = input("Enter your full name: ")
        if name not in self.accounts:
            print("Error: Account not found.")
            return
        
        pin = input("Enter your PIN: ")
        if self.accounts[name]["pin"] == pin:
            print(f"Your current balance is: ${self.accounts[name]['balance']}.")
        else:
            print("Error: Invalid PIN!")


def start():
    bank = BankSystem()
    
    while True:
        print("\n" + "="*40)
        print("WELCOME TO THE MODERN BANKING SYSTEM")
        print("="*40)
        print("1. Open a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")
        print("="*40)
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit_money()
        elif choice == '3':
            bank.withdraw_money()
        elif choice == '4':
            bank.check_balance()
        elif choice == '5':
            print("Thank you for using our services. Goodbye!")
            break
        else:
            print("Error: Unknown option. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    start()
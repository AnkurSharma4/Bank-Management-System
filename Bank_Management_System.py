class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"{self.name}'s account balance: ${self.balance}")


def main():
    accounts = {}

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                initial_deposit = float(input("Enter initial deposit (or 0): "))
                accounts[name] = Account(name, initial_deposit)
                print(f"Account created for {name}.")

        elif choice == '2':
            name = input("Enter account holder's name: ")
            if name in accounts:
                accounts[name].display_balance()
            else:
                print("Account not found.")

        elif choice == '3':
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '5':
            print("Thank you for using the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

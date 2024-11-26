# Bank Management System

## Overview
The **Bank Management System** is a simple Python application that allows users to create accounts, check balances, deposit money, and withdraw money. This system is interactive and runs in the command-line interface. 

It consists of a class `Account` that stores an account holder’s name and balance, and a `main()` function that handles user interactions, allowing for account creation, checking balances, deposits, and withdrawals.

## Features
- **Create an Account**: Allows users to create a new account by entering the account holder's name and initial deposit.
- **Check Balance**: Displays the current balance of a specific account.
- **Deposit Money**: Allows users to deposit money into their account.
- **Withdraw Money**: Allows users to withdraw money from their account, ensuring sufficient balance is available.
- **Exit the System**: Ends the session.

## Requirements
- Python 3.x

## How to Use

1. **Clone the Repository**:
   You can clone this repository to your local machine by using the following command:

   ```bash
   git clone https://github.com/yourusername/bank-management-system.git
   ```

2. **Run the Code**:
   Navigate to the directory where the `bank_management_system.py` file is located, then run the script using Python:

   ```bash
   python bank_management_system.py
   ```

3. **Interactive Menu**:
   The system will prompt you with a menu of options. Use the number keys to select different actions. Here's a brief explanation of each option:
   
   - **1. Create Account**: Create a new account by providing an account holder's name and an optional initial deposit.
   - **2. Check Balance**: Check the balance of an existing account by providing the account holder's name.
   - **3. Deposit Money**: Deposit money into an existing account.
   - **4. Withdraw Money**: Withdraw money from an existing account, ensuring the balance is sufficient.
   - **5. Exit**: Exits the system.

   Example output:
   ```bash
   --- Bank Management System ---
   1. Create Account
   2. Check Balance
   3. Deposit Money
   4. Withdraw Money
   5. Exit
   Enter your choice: 1
   Enter account holder's name: John Doe
   Enter initial deposit (or 0): 1000
   Account created for John Doe.
   ```

### Code Explanation

#### `Account` Class

```python
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
```

This class defines an account with a name and balance. It has methods for depositing, withdrawing, and displaying the balance.

#### Methods in `Account`

- **`deposit(self, amount)`**: Deposits money into the account.
- **`withdraw(self, amount)`**: Withdraws money from the account, ensuring that the balance is sufficient.
- **`display_balance(self)`**: Displays the account balance.

#### `main()` Function

This function contains the main loop, displaying an interactive menu for the user to select operations. It also handles user input and validates account existence.

```python
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

        # Handle each menu option (create account, check balance, deposit, withdraw, exit)
```

## Example Interaction

```bash
--- Bank Management System ---
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 1
Enter account holder's name: Alice
Enter initial deposit (or 0): 500
Account created for Alice.

--- Bank Management System ---
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 3
Enter account holder's name: Alice
Enter deposit amount: 200
Deposited $200. New balance: $700
```

## Contribution

If you would like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License.

---

Feel free to customize the above README based on your preferences or add more specific details such as instructions for testing or additional features.

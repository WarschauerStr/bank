# bank
creating a bank functionality using python

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/k735qCdt)
# Banking System

A **Banking System** project allows customers to manage their bank accounts using Object-Oriented Programming principles. This includes account registration, secure login, depositing and withdrawing funds, transferring money, viewing transaction history, and more.

## Topics covered
- Regular expressions
- datetime
- conditional statements
- loops
- strings 
- Prints and formatting. 
- logical operators
- basic math functions
- functions
- Command Line Interface
- Collections
- Object-Oriented Programming (OOP)
- json (saving/loading data)

## Success Criteria 

**Class creation:**

1. **Account**: Base class for general bank account.
2. **Customer**: Represents bank customers.
3. **Transaction**: Represents individual transactions (Deposit, Withdrawal, Transfer).
4. **Bank**: Manages multiple customers and accounts.

**Inheritance:**

**SavingAccount** and **CurrentAccount** classes derived from **Account**.

**Polymorphism:**

Transaction methods (deposit, withdraw, transfer) can be implemented differently for different types of accounts (e.g., saving accounts might apply interest, whereas current accounts might not).

**Encapsulation:**

Account balance and transaction details are encapsulated within the **Account** and **Transaction** classes to ensure that details are hidden from the user.

## Program structure

**Class Structure**

1. **Account**: Handles bank account operations, including depositing, withdrawing, and generating transaction statements, while tracking the account balance and storing transaction history.
2. **SavingAccount**: Inherits from Account, adds interest after each deposit.  
3. **CurrentAccount**: Inherits from Account, adds overdraft capabilities.(allowing users to withdraw more than their account balance, up to a specified overdraft limit.)
4. **Customer**: Stores customer information like username, password, and associated account(s).
   It Manages a customer's personal details, the creation of a bank account (either saving or current), and provides functionality for logging into the system using a password.
6. **Transaction**: Handles each individual transaction (Deposit, Withdrawal, Transfer). It mantains a history of all the actions taken on an account, like deposits, withdrawals, or transfers, and it helps in generating account statements.
7. **Bank**: Manages multiple customers and accounts. It is crucial for managing customer interactions and ensuring secure registration and login processes in the banking system

**Features**

1. **Deposit and Withdraw Funds**: Add or subtract money from an account.
2. **Transfer Funds**: Transfer funds between accounts.
3. **Account Statement**: Display transaction history.
4. **Simple Interest Calculation**: for Savings Accounts.
5. **Account Authentication**: Secure login with username and password.
6. **Password Management**: Authentication and password validation.

**Output example**
```
Welcome to the Bank System
1. Register a new account
2. Login to your existing account
3. Exit
Enter choice: 1

Please enter your username: federica93
Please enter your password: securePassword123@
Please enter your phone number: +491234567890
Choose account type (saving/current): saving

Registration successful for federica93
----------------------------------------------------
Welcome to the Bank System
1. Register a new account
2. Login to your existing account
3. Exit
Enter choice: 1

Please enter your username: federica93
Username already exists, please try another one.
------------------------------------------------------------
Welcome to the Bank System
1. Register a new account
2. Login to your existing account
3. Exit
Enter choice: 2

Please enter your username: federica93
Please enter your password: securePassword123@
Welcome back federica!

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 1

Enter deposit amount: 1000
Deposit successful! New balance: 1000.00 EUR

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 4

Your current balance is: 1000.00 EUR

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 5

Account Statement for federica93
---------------------------
Deposit: 1000.00 EUR, Balance after: 1000.00 EUR on 11/08/2023 #the date refers on when you made the last deposit

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 3

Enter recipient's username: jane45
Recipient not found!

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 6

Logging out...

Welcome to the Bank System
1. Register a new account
2. Login to your existing account
3. Exit
Enter choice: 2

Please enter your username: federica93
Please enter your password: securePassword123@  

Welcome back john_doe!

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 2

Enter withdrawal amount: 500
Withdrawal successful! New balance: 500.00 EUR

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 4

Your current balance is: 500.00 EUR

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 5

Account Statement for federica93
---------------------------
Deposit: 1000.00 EUR, Balance after: 1000.00 EUR on 11/08/2023
Withdrawal: 500.00 EUR, Balance after: 500.00 EUR on 11/09/2023

Please choose an option:
1. Deposit Funds
2. Withdraw Funds
3. Transfer Funds
4. Check Balance
5. Generate Statement
6. Logout
Enter choice: 6

Logging out...

Welcome to the Bank System
1. Register a new account
2. Login to your existing account
3. Exit
Enter choice: 3

Thank you for using our services!
```

**Implement Key Functionalities**

1. Registration:

- Username (ensure it’s unique).
- Password (validate that it meets certain criteria such as length, special characters, etc.). **Bonus**: When you type the password it is not shown in the terminal. 
- Phone number (with the correct number of digit and prefix).
- Account type (saving or current).
- If the username exists, prompt the user to try again with a different username.


2. Login:

- When logging in, validate the username and password against the stored customer data.
- If successful, allow access to account management options. Print a nice message. 
- If the login fails, give the user a few attempts before locking them out temporarily. **Bonus**: If the user for three times input an incorrect username or password tell the user that he has used
  all the attempts and ask the user to try again after 5 seconds(Delay your app for 5 seconds). If after that 5 seconds he enters an incorrect username or password, ask the user to register again and exit the program.

3. Deposit and Withdrawal:

- For both deposit and withdrawal, update the account balance accordingly and log the transaction.
- Ensure that the withdrawal amount does not exceed the available balance (for saving accounts) or the overdraft limit (for current accounts).

4. Transfer Funds:

- Allow a user to transfer funds to another customer's account.
- Make sure the transfer amount doesn’t exceed the balance available in the sender's account.

5. Generate Statement:

- List all transactions, including deposit, withdrawal, and transfers, along with the balance after each transaction.
- Interest Calculation (For Saving Accounts):

   - For saving accounts, interest should be added to the balance after each deposit.
   - Calculate interest based on a fixed interest rate (e.g., 2%).
  
- Overdraft Limit (For Current Accounts):

   - Ensure that withdrawals do not exceed the balance plus the overdraft limit.
   - Keep track of the overdraft status and prevent exceeding it.

6. Remember to document your code

7. Create a main function to run the banking system

8. As advance option, you could try to save accounts so they persist even after closing the program (e.g. using dict, json) you will need some research on how to do it!

**Please feel free to add additional features to your app**



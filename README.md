Banking System

This project implements a simple banking system in Python. The system allows users to:

Register as new customers.

Log in using their credentials.

Perform actions like depositing or withdrawing money after logging in.

Features

1. Customer Registration

Users provide their full name, email, phone number, and password to register.

Validation checks ensure the correctness of input (e.g., proper email format, secure password).

The user selects their account type ("saving" or "current").

Registration details are saved to a customers.json file in a specified folder.

2. Customer Login

Users log in using their email and password.

The system validates the credentials against the data in customers.json.

On successful login, users can perform various actions.

3. Post-Login Actions

After logging in, customers can:

Deposit Money: Add funds to their account.

Withdraw Money: Deduct funds from their account (only if the balance is sufficient).

Exit: Log out of the system.

4. Data Persistence

Customer data is stored in JSON format in customers.json.

Changes (e.g., balance updates) are written back to the file after every transaction.

File Structure

project_root/
|— main.py              # Entry point for the program
|— bank.py              # Contains the Bank class with core functionalities
|— validators.py       # Input validation functions
|— utils.py            # Utility functions for saving and checking data
|— customers.json      # JSON file for storing customer data

How It Works

1. Running the Program

The program starts with main.py.

It uses the Bank class from bank.py to:

Register a new user (Bank.register()).

Log in an existing user (Bank.login()).

2. Registration Workflow

Users provide required details (name, email, phone number, password).

The validators.py module checks for valid inputs:

Full name format.

Email format.

Password strength.

Phone number format.

The utils.py module ensures the phone number or email is not already registered.

User data is saved to customers.json.

3. Login Workflow

The user enters their email and password.

The system validates the credentials against customers.json.

On success, the user can perform transactions:

Deposit money.

Withdraw money (only if sufficient funds exist).

Changes to the user's balance are saved back to customers.json.

4. Data Management

The utils.py module handles file read/write operations.

Each user’s data includes:

Full name

Email

Phone number

Password

Account type (saving/current)

Balance

Registration date

How to Use

Clone or download the repository.

Place the project files in a directory of your choice.

Open a terminal and navigate to the project folder.

Run the program:

python main.py

Follow the on-screen instructions to register or log in.

Requirements

Python 3.7 or higher

Example Workflow

Registration

Enter your Name and Surname (e.g John Smith): John Doe
Enter your email (e.g example@mail.com): john.doe@gmail.com
Enter your phone number (e.g 123456789): 1234567890
Enter your password: qwertyQWE123!@#
Choose account type (saving/current): saving
Registration successful!

Login

Login:
Enter your email: john.doe@gmail.com
Enter your password: qwertyQWE123!@#

Login successful!
Welcome back, John Doe!

Please select an action:
1. Deposit money
2. Withdraw money
3. Exit

Notes

Ensure the customers.json file is in the correct directory to prevent errors.

Passwords are stored as plain text for simplicity. For production, consider encrypting sensitive data.

Input validations and checks make the system user-friendly and secure.
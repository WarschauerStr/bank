import os
import json
import re

# TODO:
# check if phone number allready exists in database
# change choose_account_type else line

# JSON path and file
# Full folder path
folder = os.path.expanduser('~/projects/all/banking_system')
filename = 'customers.json'
full_path = os.path.join(folder, filename)


class Bank:
    def __init__(
            self,
            fullname,
            email,
            password,
            phone_number,
            account_type=None,
            balance=None):

        self.fullname = fullname
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.account_type = (
            account_type if account_type else self.choose_account_type()
        )
        self.balance = balance if balance else 0

    # Choose account type
    def choose_account_type(self):
        """Ask the user for their account type."""
        decision = input(
            "Choose account type (saving/current):"
            "---> "
            )
        if decision.lower() == "saving":
            return "saving"
        elif decision.lower() == "current":
            return "current"
        else:
            print("Invalid account type. Defaulting to current.")
            return "current"

    # Save all data to JSON file
    def save_to_json(self, folder, filename):
        """Save customer data to a JSON file in a specific folder."""
        # Ensure the folder exists
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Try to read existing data from the file
        try:
            with open(full_path, 'r') as file:
                data = json.load(file)  # Load data from the JSON file
        except FileNotFoundError:
            # If file doesn't exist, initialize an empty list
            data = []

        # Create a dictionary for the customer
        customer_data = {
            'fullname': self.fullname,
            'email': self.email,
            'password': self.password,
            'phone_number': self.phone_number,
            'account_type': self.account_type,
            'balance': self.balance,
        }

        # Append the customer data to the list
        data.append(customer_data)

        # Write the updated data back to the JSON file
        with open(full_path, 'w') as file:
            json.dump(data, file, indent=4)

    # Validate full name format
    @staticmethod
    def validate_fullname(fullname):
        # Define our regex pattern for validation
        pattern = r"^[A-Za-z]+ [A-Za-z]+$"
        # We use the re.match function to test the fullname against the pattern
        match = re.match(pattern, fullname)
        # Return True if the fullname matches the pattern, False otherwise
        return bool(match)

    # Check if emain already registered
    @classmethod
    def check_email_registered(cls, email, folder, filename):
        # Ensure file path is correctly defined
        try:
            with open(full_path, 'r') as file:
                customers = json.load(file)
        except FileNotFoundError:
            print("No customer data found!")
            return False  # Return False if the file doesn't exist

        # Check if the email already exists in the JSON file
        for customer in customers:
            if customer['email'] == email:
                return True
        return False  # Only return False if no matching email is found

    # Validate email format
    @staticmethod
    def validate_email(email):
        # Define our regex pattern for validation
        pattern = r"^\S+@\S+\.\S+$"
        # We use the re.match function to test the email against the pattern
        match = re.match(pattern, email)
        # Return True if the email matches the pattern, False otherwise
        return bool(match)

    # Check password security level
    @staticmethod
    def validate_password(password):
        # Define our regex pattern for validation
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
        # We use the re.match function to test the password against the pattern
        match = re.match(pattern, password)
        # Return True if the password matches the pattern, False otherwise
        return bool(match)

    # Validate phone number format
    @staticmethod
    def validate_phone_number(phone_number):
        # Define our regex pattern for validation
        pattern = r"^[1-9][0-9]{7,14}$"
        # We use the re.match function to test --->
        # the phone number against the pattern
        match = re.match(pattern, phone_number)
        # Return True if the phone number matches the pattern, False otherwise
        return bool(match)

    # Registrate new customer
    @classmethod
    def register(cls, folder, filename):
        # Ask fullname
        fullname = input(
            "Enter your Name and Surname:\n"
            "e.g John Smith\n"
            "---> "
            ).title()
        while not cls.validate_fullname(fullname):
            print("Invalid name. Please try again.")
            fullname = input()

        # Check if email is already registered
        email = input(
            "Enter your email:\n"
            "e.g. example@mail.com\n"
            "---> "
            )
        while not cls.validate_email(email):
            print("Invalid email. Please try again.")
            email = input()
        while cls.check_email_registered(email, folder, filename):
            print("Email already registered. Please try again.")
            email = input()

        # Check password security level
        password = input(
            "Enter your password:\n"
            "* Has minimum 8 characters in length.\n"
            "* At least one uppercase English letter.\n"
            "* At least one digit.\n"
            "* At least one special character.\n"
            "---> "
            )
        while not cls.validate_password(password):
            print("Password is too weak. Please try again.")
            password = input()

        # Check phone number format
        phone_number = input(
            "Enter your phone number:\n"
            "e.g. 123456789\n"
            "---> "
            )
        while not cls.validate_phone_number(phone_number):
            print("Invalid phone number. Please try again.")
            phone_number = input()

        print("Registration successful!")

        # Create a new customer instance
        new_customer = cls(fullname, email, password, phone_number)

        # Save customer data to the JSON file in the specified folder
        new_customer.save_to_json(folder, filename)

    # Print all registered customers from the JSON file
    @classmethod
    def print_all_customers(cls, folder, filename):
        """Print all registered customers from the JSON file."""
        # Try to read data from the JSON file
        try:
            with open(full_path, 'r') as file:
                customers = json.load(file)
        except FileNotFoundError:
            print("No customer data found!")
            return

        # Print out each customer's details
        if customers:
            print("Registered Customers:")
            for customer in customers:
                print(
                    f"Name: {customer['fullname']}, "
                    f"Email: {customer['email']}, "
                    f"Account Type: {customer['account_type']}"
                )
        else:
            print("No customers registered yet.")

    # Handle customer login and provide appropriate responses
    @classmethod
    def login(cls, folder, filename):
        """Handle customer login."""
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Try to read data from the JSON file
        try:
            with open(full_path, 'r') as file:
                customers = json.load(file)
        except FileNotFoundError:
            print("No customer data found!")
            return

        # Check if the email and password match any customer data
        for customer in customers:
            if customer['email'] == email and customer['password'] == password:
                print(
                    "Login successful!\n"
                    f"Welcome back, {customer[f'fullname']}!"
                    )
                return
        print("Invalid email or password!")


# Print all registered customers
# Bank.print_all_customers(folder, filename)

# Registrate new customer
# Bank.register(folder, filename)

# Login
# Bank.login(folder, filename)

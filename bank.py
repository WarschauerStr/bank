from validators import (
    validate_fullname,
    validate_email,
    validate_password,
    validate_phone_number
    )

from utils import (
    save_to_json,
    check_phone_and_email_exists
    )

import json
import os
from datetime import datetime


class Bank:
    def __init__(
            self,
            fullname,
            email,
            password,
            phone_number,
            balance=0,
            account_type=None,
            regestration_date=None):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.account_type = (
            account_type if account_type else self.choose_account_type()
        )
        self.balance = balance if balance else 0
        self.regestration_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def choose_account_type(self):
        """Ask the user for their account type."""
        decision = input("Choose account type (saving/current): ")
        if decision.lower() == "saving":
            return "saving"
        elif decision.lower() == "current":
            return "current"
        else:
            print("Invalid account type. Defaulting to current.")
            return "current"

    @classmethod
    def register(self, folder, filename):
        """Handle customer registration."""
        fullname = (
            input("Enter your Name and Surname (e.g John Smith): ").title()
        )
        while not validate_fullname(fullname):
            print("Invalid name. Please try again.")
            fullname = input()

        email = input("Enter your email (e.g example@mail.com): ")
        while not validate_email(email):
            print("Invalid email. Please try again.")
            email = input()

        phone_number = input("Enter your phone number (e.g 123456789): ")
        while not validate_phone_number(phone_number):
            print("Invalid phone number. Please try again.")
            phone_number = input()

        while check_phone_and_email_exists(
            phone_number, email, folder, filename
        ):
            print(
                "Email or phone number already registered. Please try again."
                )
            email = input("Enter your email (e.g example@mail.com): ")
            while not validate_email(email):
                print("Invalid email. Please try again.")
                email = input()
            phone_number = input("Enter your phone number (e.g 123456789): ")
            while not validate_phone_number(phone_number):
                print("Invalid phone number. Please try again.")
                phone_number = input()

        password = input("Enter your password: ")
        while not validate_password(password):
            print("Password is too weak. Please try again.")
            password = input()

        print("Registration successful!")

        new_customer = Bank(fullname, email, password, phone_number)
        save_to_json(new_customer, folder, filename)

    @classmethod
    def login(cls, folder, filename):
        """Handle customer login."""
        full_path = os.path.join(folder, filename)
        customers = cls._load_customer_data(full_path)

        if not customers:
            print("No customer data found!")
            return

        customer = cls._authenticate_user(customers)
        if customer:
            cls._handle_post_login_actions(customer, full_path, customers)

    @staticmethod
    def _load_customer_data(full_path):
        """Load customer data from the JSON file."""
        try:
            with open(full_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def _authenticate_user(customers):
        """Authenticate the user by email and password."""
        print("Login:")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for customer in customers:
            if customer['email'] == email and customer['password'] == password:
                print(
                    f"\nLogin successful!\n"
                    f"Welcome back, {customer['fullname']}!\n"
                )
                return customer

        print("Invalid email or password. Please try again.")
        return None

    @staticmethod
    def _handle_post_login_actions(customer, full_path, customers):
        """Handle deposit, withdrawal, and other actions post-login."""
        while True:
            print(
                "\nPlease select an action:\n"
                "1. Deposit money\n"
                "2. Withdraw money\n"
                "3. Exit\n"
            )
            choice = input("Enter your choice: (e.g. 1, 2, 3): ")

            if choice == "1":
                Bank._deposit_money(customer, full_path, customers)
            elif choice == "2":
                Bank._withdraw_money(customer, full_path, customers)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def _deposit_money(customer, full_path, customers):
        """Handle deposit action."""
        amount = input("\nEnter amount that you want to deposit: ")
        try:
            amount = float(amount)
            customer["balance"] += amount
            print(f"Balance updated. New balance: ${customer['balance']}")
            with open(full_path, 'w') as file:
                json.dump(customers, file, indent=4)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    @staticmethod
    def _withdraw_money(customer, full_path, customers):
        """Handle withdrawal action."""
        amount = input("Enter amount that you want to withdraw: ")
        try:
            amount = float(amount)
            if amount > customer["balance"]:
                print("Not enough money on the account.")
            else:
                customer["balance"] -= amount
                print(f"Balance updated. New balance: ${customer['balance']}")
                with open(full_path, 'w') as file:
                    json.dump(customers, file, indent=4)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

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
            account_type=None,
            balance=None,
            regestration_date=None):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.account_type = (
            account_type if account_type else self.choose_account_type()
        )
        self.balance = balance if balance else 0
        self.regestration_date = datetime.now().strftime("%Y-%m-%d")

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
        print("Login:")
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

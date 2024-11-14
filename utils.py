import os
import json


def save_to_json(bank_instance, folder, filename):
    """Save customer data to the JSON file in a specific folder."""
    full_path = os.path.join(folder, filename)
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        with open(full_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    customer_data = {
        'fullname': bank_instance.fullname,
        'email': bank_instance.email,
        'password': bank_instance.password,
        'phone_number': bank_instance.phone_number,
        'account_type': bank_instance.account_type,
        'balance': bank_instance.balance,
        'registration_date': bank_instance.regestration_date
    }

    data.append(customer_data)

    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)


def check_phone_and_email_exists(phone_number, email, folder, filename):
    full_path = os.path.join(folder, filename)
    try:
        with open(full_path, 'r') as file:
            customers = json.load(file)
    except FileNotFoundError:
        return False

    for customer in customers:
        if (customer['phone_number'] == phone_number or
                customer['email'] == email):
            return True
    return False

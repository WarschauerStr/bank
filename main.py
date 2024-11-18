from bank import Bank
import os

folder = os.path.expanduser('~/projects/all/banking_system')
filename = "customers.json"


customer = Bank.login(folder, filename)
if customer == "Error":
    print("Invalid email or password. Please try again.")
else:
    while True:
        bank = Bank(customer)
        print(
            f"\nWelcome back, {bank.fullname}!\n"
            f"Current balance: ${bank.balance}\n"
        )


# Registrate new customer
# Bank.register(folder, filename)

# Login
# Bank.login(folder, filename)

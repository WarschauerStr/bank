from bank import Bank
import os

folder = os.path.expanduser('~/projects/all/banking_system')
filename = "customers.json"


# Main menu for interacting with the bank system
def main():
    while True:
        print(
            "\nWelcome to the Bank System!\n"
            "1. Register\n"
            "2. Login\n"
            "3. Exit\n"
        )
        choice = input("Enter your choice: (e.g. 1, 2, 3): ")

        if choice == "1":
            Bank.register(folder, filename)
        elif choice == "2":
            Bank.login(folder, filename)
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

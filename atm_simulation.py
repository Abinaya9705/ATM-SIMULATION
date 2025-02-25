import datetime

class ATMMachine:
    def __init__(self):
        """Initialize user account details, including balance, PIN, and transaction history."""
        self.balance = 5000  # Initial account balance
        self.pin = "1234"  # Default PIN
        self.transaction_history = []  # Stores transaction details

    def check_balance(self):
        """Displays the current account balance."""
        print(f"\nYour current balance is: ₹{self.balance}")
        self.transaction_history.append(f"{datetime.datetime.now()} - Balance Inquiry: ₹{self.balance}")

    def deposit_cash(self):
        """Allows the user to deposit cash into their account."""
        amount = int(input("\nEnter amount to deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
            self.transaction_history.append(f"{datetime.datetime.now()} - Deposited: ₹{amount}")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw_cash(self):
        """Allows the user to withdraw cash from their account."""
        amount = int(input("\nEnter amount to withdraw: ₹"))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
            self.transaction_history.append(f"{datetime.datetime.now()} - Withdrawn: ₹{amount}")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Invalid amount. Please enter a positive value.")

    def change_pin(self):
        """Allows the user to change their PIN."""
        old_pin = input("\nEnter current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully!")
                self.transaction_history.append(f"{datetime.datetime.now()} - PIN Changed")
            else:
                print("PIN confirmation does not match!")
        else:
            print("Incorrect current PIN!")

    def view_transaction_history(self):
        """Displays the transaction history of the user."""
        print("\nTransaction History:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def start(self):
        """Main function to simulate ATM operations."""
        print("Welcome to the ATM!\n")
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            while True:
                print("\n--- ATM MENU ---")
                print("1. Check Balance")
                print("2. Deposit Cash")
                print("3. Withdraw Cash")
                print("4. Change PIN")
                print("5. View Transaction History")
                print("6. Exit")

                choice = input("\nSelect an option (1-6): ")

                if choice == "1":
                    self.check_balance()
                elif choice == "2":
                    self.deposit_cash()
                elif choice == "3":
                    self.withdraw_cash()
                elif choice == "4":
                    self.change_pin()
                elif choice == "5":
                    self.view_transaction_history()
                elif choice == "6":
                    print("Thank you for using the ATM. Have a great day!")
                    break
                else:
                    print("Invalid choice! Please select a valid option.")
        else:
            print("Incorrect PIN. Access denied.")

# Start the ATM simulation
atm = ATMMachine()
atm.start()

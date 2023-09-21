class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Number: {self.__account_number}\nAccount Holder: {self.__account_holder_name}\nAccount Balance: ${self.__account_balance:.2f}"


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("766554", "Sornamala", 56557.0)

    # Display the initial account balance
    print("Initial Account Balance:")
    print(account.display_balance())

    # Deposit $500
    if account.deposit(7000.0):
        print("\n$7000 deposited successfully.")
    else:
        print("\nInvalid deposit amount.")

    # Display updated account balance
    print("\nAccount Balance after Deposit:")
    print(account.display_balance())

    # Withdraw $200
    if account.withdraw(770.0):
        print("\n$770 withdrawn successfully.")
    else:
        print("\nInsufficient balance or invalid withdrawal amount.")

    # Display updated account balance
    print("\nAccount Balance after Withdrawal:")
    print(account.display_balance())

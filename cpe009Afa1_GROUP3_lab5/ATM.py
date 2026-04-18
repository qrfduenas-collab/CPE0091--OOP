class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = []

    def deposit(self, account, amount):
        account.current_balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, account, amount):
        if amount <= account.current_balance:
            account.current_balance -= amount
            self.transactions.append(f"Withdrew {amount}")
        else:
            print("Insufficient balance")

    def check_currentbalance(self, account):
        return account.current_balance

    def view_transactionsummary(self):
        print("Transaction Summary:")
        for t in self.transactions:
            print(t)


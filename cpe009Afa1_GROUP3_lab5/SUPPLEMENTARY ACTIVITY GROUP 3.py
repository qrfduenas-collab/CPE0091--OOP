#GROUP 3
#ACCOUNT
class Accounts:
    def __init__(self, account_number, firstname, lastname, balance, address, email):
        self.account_number = account_number
        self.account_firstname = firstname
        self.account_lastname = lastname
        self.current_balance = balance
        self.address = address
        self.email = email

    def update_address(self, new_address):
        self.address = new_address

    def update_email(self, new_email):
        self.email = new_email
#ATM
class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = []

    def deposit(self, account, amount):
        account.current_balance += amount
        self.transactions.append("Deposited " + str(amount))

    def withdraw(self, account, amount):
        if amount <= account.current_balance:
            account.current_balance -= amount
            self.transactions.append("Withdrew " + str(amount))
        else:
            print("Insufficient balance")

    def check_currentbalance(self, account):
        return account.current_balance

    def view_transactionsummary(self):
        print("\nTransaction Summary:")
        for t in self.transactions:
            print(t)
#MAIN
account1 = Accounts(1, "Ralph", "Duenas", 1000, "Quezon City", "ralph@email.com")
account2 = Accounts(2, "John", "Doe", 500, "Manila", "john@email.com")

atm1 = ATM(987654)

atm1.deposit(account1, 500)
atm1.withdraw(account2, 200)

print(account1.account_firstname, "Balance:", account1.current_balance)
print(account2.account_firstname, "Balance:", account2.current_balance)

print("ATM Serial Number:", atm1.serial_number)

atm1.view_transactionsummary()
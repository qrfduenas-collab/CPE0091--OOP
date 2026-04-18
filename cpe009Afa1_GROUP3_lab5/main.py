from Accounts import Accounts
from ATM import ATM

# Create account objects
account1 = Accounts(1, "Ralph", "Duenas", 1000, "Quezon City", "ralph@email.com")
account2 = Accounts(2, "John", "Doe", 500, "Manila", "john@email.com")

# Create ATM object
atm1 = ATM(123456)

# Perform transactions
atm1.deposit(account1, 500)
atm1.withdraw(account2, 200)

# Check balances
print(account1.account_firstname, "Balance:", account1.current_balance)
print(account2.account_firstname, "Balance:", account2.current_balance)

# Show ATM serial number
print("ATM Serial Number:", atm1.serial_number)

# Show transactions
atm1.view_transactionsummary()
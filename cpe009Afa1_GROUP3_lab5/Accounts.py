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
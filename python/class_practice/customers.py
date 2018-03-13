class Customer(object):

    """ Created customer class for customer objects.

    Attributes:
    - name: creates a string holding the customers name
    - balance: creates float that holds customers balance relating
    to customer name"""

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return RuntimeError('Cannot take out this amount')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
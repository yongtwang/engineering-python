# piggy.py
# The class definition for a piggy bank.
class Piggy:
    def __init__(self):  
        self.balance = 0  # The starting balance is $0.

    def get_balance(self):
        return self.balance

    def deposit(self, amount): 
        if amount < 0:
            print('The amount cannot be negative.')
        elif self.balance + amount > 100:
            print('Not enough space for this amount.')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print('The amount cannot be negative.')
        elif self.balance - amount < 0:
            print('The amount is more than the balance.')
        else:
            self.balance -= amount
from datetime import date
class Transaction:
    def __init__(self, amount):
        if type(amount) != int:
            raise Exception("Input must be an integer")
        self.amount = amount
